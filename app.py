import streamlit as st
import ollama
import fitz  # PyMuPDF for PDF reading
import docx  # for DOCX resume reading

st.set_page_config(page_title="AI Career Coach", layout="wide")
st.title("🧠 AI Career Coach")
st.write("Boost your career with AI-powered resume, cover letter, and interview tools.")

menu = st.sidebar.radio("Choose a module", ["Resume Enhancer", "Cover Letter Generator", "Interview Coach"])

# --- Ollama Call Function ---
def call_gpt(prompt, model="llama2", temperature=0.7):
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temperature}
        )
        return response['message']['content']
    except Exception as e:
        return f"❌ Error from Ollama: {str(e)}"

# --- Resume Text Extraction ---
def extract_resume_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

# === MODULE 1: Resume Enhancer ===
if menu == "Resume Enhancer":
    uploaded_file = st.file_uploader("Upload your resume (.pdf or .docx)", type=["pdf", "docx"])
    job_title = st.text_input("Target Job Title (e.g., Data Analyst)")
    resume_text = ""

    if uploaded_file:
        resume_text = extract_resume_text(uploaded_file)
        st.success("✅ Resume text extracted!")
        st.text_area("Extracted Resume", value=resume_text, height=250)

    if st.button("Enhance Resume"):
        if resume_text and job_title:
            prompt = f"Rewrite this resume to align with a {job_title} role. Make it more impactful, clear, and role-specific:\n\n{resume_text}"
            result = call_gpt(prompt)
            st.subheader("🔍 Enhanced Resume:")
            st.text_area("Output", result, height=300)
        else:
            st.warning("Please upload a resume and enter a job title.")

# === MODULE 2: Cover Letter Generator ===
elif menu == "Cover Letter Generator":
    uploaded_file = st.file_uploader("Upload your resume again (.pdf or .docx)", type=["pdf", "docx"], key="cl")
    company = st.text_input("Company Name")
    job_title = st.text_input("Job Title")
    job_description = st.text_area("Paste the job description")
    resume_text = ""

    if uploaded_file:
        resume_text = extract_resume_text(uploaded_file)

    if st.button("Generate Cover Letter"):
        if resume_text and company and job_title and job_description:
            prompt = f"""Write a professional cover letter for the position of {job_title} at {company}. Use the resume and job description below.
Resume:
{resume_text}
Job Description:
{job_description}"""
            result = call_gpt(prompt)
            st.subheader("📝 Generated Cover Letter:")
            st.text_area("Output", result, height=300)
        else:
            st.warning("Please fill in all fields and upload your resume.")

# === MODULE 3: Interview Coach ===
elif menu == "Interview Coach":
    role = st.text_input("Enter the Role (e.g., Product Manager, Data Analyst)")
    if st.button("Get Sample Interview Questions"):
        prompt = f"Give me 5 common interview questions with model answers for a {role} role."
        result = call_gpt(prompt)
        st.subheader("🎤 Interview Q&A:")
        st.markdown(result)
