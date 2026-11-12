"""AI Audiobook Generator.

A Streamlit app that extracts text from PDF / DOCX / TXT files and converts it
into an MP3 audiobook using Google Text-to-Speech (gTTS).
"""

import io
import re

import pdfplumber
import streamlit as st
from docx import Document
from gtts import gTTS

LANGUAGE = "en"
MAX_CHUNK_CHARS = 4500  # keeps each gTTS request to a safe size


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def extract_text(file) -> str:
    """Return plain text from a PDF, DOCX or TXT upload."""
    name = file.name.lower()

    if name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    if name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    if name.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    return ""


def split_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split text into chunks (on sentence boundaries) of at most max_chars."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        # Hard-split any single sentence that is longer than the limit.
        while len(sentence) > max_chars:
            if current:
                chunks.append(current)
                current = ""
            chunks.append(sentence[:max_chars])
            sentence = sentence[max_chars:]

        if len(current) + len(sentence) + 1 > max_chars:
            chunks.append(current)
            current = sentence
        else:
            current = f"{current} {sentence}".strip()

    if current:
        chunks.append(current)
    return chunks


def text_to_mp3(text: str, progress=None) -> bytes:
    """Convert text to MP3 bytes, chunking long text to avoid gTTS failures."""
    chunks = split_text(text)
    buffer = io.BytesIO()

    for i, chunk in enumerate(chunks, start=1):
        gTTS(text=chunk, lang=LANGUAGE).write_to_fp(buffer)
        if progress is not None:
            progress.progress(i / len(chunks), text=f"Converting part {i} of {len(chunks)}...")

    return buffer.getvalue()


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
def main() -> None:
    st.title("AI Audio Book Generator 🎧")
    st.write("Upload a PDF / DOCX / TXT file and convert it into an MP3 audiobook.")

    uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx", "txt"])
    if uploaded_file is None:
        return

    st.success(f"File uploaded: {uploaded_file.name}")

    # Step 1: extract text
    if st.button("1️⃣ Extract Text"):
        with st.spinner("Extracting text from file..."):
            text = extract_text(uploaded_file)

        if not text.strip():
            st.error("No text could be extracted from this file.")
        else:
            st.session_state["text_editor"] = text
            st.session_state.pop("audio_bytes", None)
            st.success("Text extracted successfully!")

    # The editor lives outside the button block so it persists across reruns.
    if "text_editor" in st.session_state:
        st.text_area(
            "Extracted Text (you can edit this before converting to audio):",
            key="text_editor",
            height=300,
        )

    # Step 2: convert to audio
    if st.button("2️⃣ Convert to Audio 🎧"):
        text = st.session_state.get("text_editor", "")
        if not text.strip():
            st.error("No text available. First upload a file and click 'Extract Text'.")
        else:
            progress = st.progress(0.0, text="Generating audio...")
            try:
                st.session_state["audio_bytes"] = text_to_mp3(text, progress)
                st.success("Audio generated successfully!")
            except Exception as exc:  # network/gTTS errors
                st.error(f"Audio generation failed: {exc}")
            finally:
                progress.empty()

    # Player + download (kept in session_state so it survives reruns)
    audio_bytes = st.session_state.get("audio_bytes")
    if audio_bytes:
        st.audio(audio_bytes, format="audio/mp3")
        st.download_button(
            label="Download Audiobook (MP3)",
            data=audio_bytes,
            file_name="audiobook.mp3",
            mime="audio/mpeg",
        )


main()
