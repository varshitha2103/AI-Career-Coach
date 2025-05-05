# 🧠 AI Career Coach

**AI Career Coach** is a simple Streamlit web app that helps users enhance resumes, generate cover letters, and prepare for interviews using locally running AI models like `LLaMA 2`, `Mistral`, or `Phi` via [Ollama](https://ollama.com/). No internet APIs or billing needed — everything runs on your own machine.

---

## 🚀 Features

- 📄 **Resume Enhancer** – Rewrites and improves resumes for any target job role
- ✉️ **Cover Letter Generator** – Creates personalized cover letters from resume + job description
- 🎤 **Interview Coach** – Generates common Q&A for technical and behavioral interviews
- 📎 **Supports File Uploads** – Accepts `.pdf` and `.docx` resumes
- 🧠 Powered by local LLMs: `phi`, `llama2`, `mistral`, etc. via Ollama

---

## 🛠️ Requirements

- Python 3.8+
- Ollama (for running local LLMs)
- Streamlit
- Basic system RAM: 4–8 GB (varies by model)

---

## 🔧 Installation

1. **Clone this repository** or download the code:

```bash
git clone https://github.com/yourusername/ai-career-coach.git
cd ai-career-coach
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install and run Ollama:

Download: https://ollama.com/download

Then run your chosen model (example: llama2 or phi)

bash
Copy
Edit
ollama run llama2
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501

🤖 Supported Models
You can change the model used by editing app.py:

python
Copy
Edit
call_gpt(prompt, model="llama2")
Recommended:

phi – lightweight, very fast (~1.8GB RAM)

mistral – better quality, needs ~6–8GB RAM

llama2 – more fluent and accurate (~8–10GB RAM)

⚠️ Choose a model that fits your available system memory.

📁 Project Structure
arduino
Copy
Edit
ai-career-coach/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .streamlit/
│   └── config.toml       # (optional) Streamlit UI config
🧠 Sample Use Case
Upload your resume as PDF or DOCX

Enter your target job role (e.g., "Data Analyst")

Click "Enhance Resume" to generate AI-enhanced content

Use other modules to generate cover letters or interview Q&A

📜 License
MIT License — free to use, share, or modify.

🙋‍♀️ Author
Developed by Varshitha Yanamala
Powered by Ollama + Streamlit
