import streamlit as st
import pdfplumber
from docx import Document
from gtts import gTTS
import tempfile

# Title and description
st.title("AI Audio Book Generator 🎧")
st.write("Upload a PDF / DOCX / TXT file and convert it into an MP3 audiobook.")

# ---- File upload ----
uploaded_file = st.file_uploader(
    "Upload your file",
    type=["pdf", "docx", "txt"]
)

def extract_text(file):
    """Return plain text from PDF, DOCX or TXT file."""
    name = file.name.lower()

    # PDF
    if name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
        return text

    # DOCX
    if name.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    # TXT
    if name.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    return ""

# ---- Main UI logic ----
if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")

    # 1) Extract text button
    if st.button("1️⃣ Extract Text"):
        with st.spinner("Extracting text from file..."):
            text = extract_text(uploaded_file)

        if not text.strip():
            st.error("No text could be extracted from this file.")
        else:
            # store in session_state so we can reuse it for audio
            st.session_state["text_data"] = text
            st.success("Text extracted successfully!")
            st.text_area(
                "Extracted Text (you can edit this before converting to audio):",
                text,
                height=300
            )

# 2) Convert to audio button
if st.button("2️⃣ Convert to Audio 🎧"):
    text = st.session_state.get("text_data", "")

    if not text.strip():
        st.error("No text available. First upload a file and click 'Extract Text'.")
    else:
        with st.spinner("Generating audio..."):
            tts = gTTS(text=text, lang="en")
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(tmp.name)

        st.success("Audio generated successfully!")

        # play audio
        audio_bytes = open(tmp.name, "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

        # download button
        st.download_button(
            label="Download Audiobook (MP3)",
            data=audio_bytes,
            file_name="audiobook.mp3",
            mime="audio/mpeg"
        )