# 🎧 AI Audiobook Generator

A simple, user-friendly web app that converts text documents into MP3 audiobooks.

Upload a **PDF**, **DOCX**, or **TXT** file, and the app extracts the text and converts it to audio using **Google Text-to-Speech (gTTS)**. It's especially helpful for students, readers, and visually impaired users who prefer listening to reading.

---

## 🚀 Features

- Upload PDF, DOCX, and TXT files
- Automatic text extraction
- Text-to-speech conversion to MP3
- Listen to the audio directly in the browser
- Download the generated audiobook
- Clean, simple Streamlit interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| Python 3 | Core language |
| Streamlit | Web interface |
| pdfplumber | PDF text extraction |
| python-docx | DOCX reading |
| gTTS | Text-to-speech |
| Pillow / pypdfium2 | PDF dependencies |

---

## 📂 Project Structure

```text
Audio_book-generator/
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pavangollavilli7/Audio_book-generator.git
   cd Audio_book-generator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Start the app:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`), upload a document, and generate your audiobook.

---

## 🔄 How It Works

1. The user uploads a file (PDF, DOCX, or TXT).
2. Text is extracted using `pdfplumber` (PDF) or `python-docx` (DOCX).
3. The text is processed and cleaned.
4. `gTTS` converts the text into speech.
5. The app generates an MP3 audiobook.
6. The user plays it in the browser or downloads the file.

---

## ⚠️ Limitations

- gTTS requires an internet connection.
- Very long documents may fail or be slow, since long-text splitting is not yet supported.

---

## 🔮 Future Enhancements

- [ ] Multiple voice options
- [ ] Long PDF splitting
- [ ] Language translation with multilingual audio
- [ ] Background music
- [ ] Deployment on Streamlit Cloud

---

## ✅ Conclusion

This project shows how Python can turn documents into audiobooks. It is simple, efficient, and helpful for students, readers, and visually impaired users.
