# 🎧 AI Audiobook Generator

The **AI Audiobook Generator** is a simple and user-friendly web application that converts text documents into MP3 audiobooks.  
Users can upload **PDF**, **DOCX**, or **TXT** files, and the system extracts the text and converts it into audio using **Google Text-to-Speech (gTTS)**.

This tool is especially helpful for students, readers, and visually impaired users who prefer listening instead of reading.

---

## 🚀 Features

✔ Upload PDF, DOCX, and TXT files  
✔ Extract text automatically  
✔ Convert extracted text to MP3 audio  
✔ Listen to the audio directly in the browser  
✔ Download the audiobook file  
✔ Clean and simple Streamlit interface  

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – Web interface  
- **pdfplumber** – PDF text extraction  
- **python-docx** – DOCX reading  
- **gTTS** – Text-to-speech  
- **Pillow / pypdfium2** – PDF dependencies

---

## 📂 Project Structure
AI-Audiobook-Generator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── samples/
│ ├── sample.pdf
│ ├── sample.txt
│ └── sample.docx
│
└── output/
└── sample_audio.mp3

✔ 1. Installation Instructions
🛠 Installation
To install the required dependencies, run:
pip install -r requirements.txt
To run the Streamlit app:
streamlit run app.py

✔ 2. How the Project Works
🚀 How It Works
1)User uploads a file (PDF / DOCX / TXT)
2)Text is extracted using pdfplumber / python-docx
3)The text is processed
4)gTTS converts text into speech
5)The app generates an MP3 audiobook
6)User can download the audio file

🔮 Future Enhancements
* Add multiple voice options
* Support long PDF splitting
* Add language translation + multilingual audio
* Add background music
* Deploy on Streamlit Cloud


### ✅ Conclusion
This project demonstrates how AI and Python can convert documents into interactive audiobooks. 
It is simple, efficient, and helpful for students, readers, and visually impaired users.
