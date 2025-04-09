# 🎓 YouTube Lecture Summarizer Microagent

Turn any YouTube lecture into clean, concise study notes and quizzes — all with a single click!

![App Screenshot](https://github.com/siddhiipatell/youtube-lecture-summarizer-microagent/raw/main/assets/demo.gif)

## 🧠 What is it?

This Streamlit-based AI microagent allows you to:
- Extract transcripts from YouTube lectures
- Generate structured lecture notes
- Create quiz questions
- Download everything as a neat PDF

Perfect for students, educators, or lifelong learners who want to **learn smarter, not harder**.

## 🚀 Features

- 📄 **Transcript Extraction** from YouTube videos
- ✍️ **AI-Powered Summarization** into clear lecture notes
- ❓ **Quiz Generation** to test understanding
- 📥 **PDF Export** of notes and questions
- ⚡️ Built with LLMs and modular utilities

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Utilities**: OpenAI LLM (for summarization and quiz)
- **PDF Generation**: ReportLab
- **Transcripts**: `youtube-transcript-api`

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/siddhiipatell/youtube-lecture-summarizer-microagent.git
cd youtube-lecture-summarizer-microagent
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Ollama base URL and model name (used for summarization and quiz)

Ollama runs on localhost:11434 by default:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_MODEL=llama3  # You can use llama2, mistral, or any model you've pulled
```

optionally in ```.env```

```bash
# .env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3 # You can use llama2, mistral, or any model you've pulled
```

Run the app:

```bash
streamlit run app.py
```

## 🧪 Example Usage
1. Paste a YouTube lecture URL
2. Let the agent fetch and summarize the transcript
3. View notes and auto-generated quiz
4. Download it all as a PDF

## 📁 Project Structure

```bash
├── app.py                     # Streamlit app interface
├── utils/
│   ├── transcript_utils.py    # Gets transcript from YouTube
│   ├── summarizer.py          # AI summarization logic
│   ├── quiz_generator.py      # AI quiz generation
│   └── pdf_generator.py       # Markdown → PDF conversion
├── requirements.txt
└── README.md
```

## 🙌 Contributing
Pull requests are welcome! If you find a bug or want to suggest a feature, feel free to open an issue.

## 📄 License
This project is licensed under the MIT License.

## ✨ Acknowledgements
- OpenAI
- Streamlit
- youtube-transcript-api

