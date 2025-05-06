# 🧠 AI Career Coach

**AI Career Coach** is a Streamlit-powered web app that uses Meta’s **LLaMA 2** via [Ollama](https://ollama.com) to help job seekers enhance resumes, generate personalized cover letters, and practice interview questions. Everything runs **locally** — no API key or internet access required.

---

## 🚀 Features

- 📄 Resume Enhancer – AI-polished resumes for any target job role
- ✉️ Cover Letter Generator – Personalized letters based on resume + job description
- 🎤 Interview Coach – Generates Q&A tailored to the job role
- 📎 Supports PDF and DOCX resume uploads
- 🤖 Uses local LLaMA 2 model via Ollama

---

## 🛠 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/download)
- Streamlit
- 8 GB RAM (recommended for LLaMA 2)

---

## 🔧 Installation

1. **Clone the repository**

git clone https://github.com/yourusername/ai-career-coach.git
cd ai-career-coach


2. **Create a virtual environment**

python -m venv venv

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Install and start LLaMA 2 using Ollama**

ollama run llama2

---

## ▶️ Run the App

streamlit run app.py


Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 Change Model (Optional)

You can use other Ollama models by editing this line in `app.py`:

```python
response = ollama.chat(model="llama2", ...)

Try:

phi (very lightweight)

mistral (high quality, needs more RAM)

llama2:7b-chat-q4_0 (quantized, lower memory)

📁 Project Structure

ai-career-coach/
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml (optional)


🙋‍♀️ Author
Built by Varshitha Yanamala

Powered by:

Ollama

Streamlit

LLaMA 2 by Meta


---

Let me know if you'd like me to save this into a downloadable `.md` file or help you structure the GitHub repo itself.







