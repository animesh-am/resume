from pathlib import Path

import streamlit
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# -------GENERAL SETTINGS-------
PAGE_TITLE = "DIGITAL RESUME | ANIMESH MAITY"
PAGE_ICON = "🪁"
NAME = "ANIMESH MAITY"
DESCRIPTION = """
Aspiring BCA graduate seeking a dynamic role to apply skills in active projects, with a keen
interest in building a career in data"""
EMAIL = "animesh.maity.iam@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/animesh-maity",
    "Github": "https://github.com/animesh-am",
}

PROJECTS = {
    "🏆 Loan Prediction, Speech Emotion Recognition, Uber Data Analysis": "https://github.com/animesh-am/CodeClause_Internship",
    "🏆 Groundnut Disease Classifier WebApp": "https://github.com/animesh-am/Groundnut-Disease-Classifier",
    "🏆 Student Management System using C": "https://github.com/animesh-am/student-management-system",
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# ---LOAD CSS, PDF, PROFILE-PIC---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---HERO SECTION---
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width = 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
            label = "⬇ Download Resume",
            data = PDFbyte,
            file_name = resume_file.name,
            mime = "application/octed_stream",
    )
    st.write("📧", EMAIL)

# ---SOCIAL LINKS---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---EXPERIENCE & QUALIFICATIONS---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
        """
        - ✅ Basic Understanding about C and Python.
        - ✅ Basic Understanding in Convolution Neural Network and Deep Learning.
        - ✅ Worked as a team and analyzed Research Papers.
        - ✅ Advised a hypothetical client as a Data Analyst at Accenture in Virtual Internship.
        """
)

# ---SKILLS---
st.write("#")
st.subheader("Hard Skills")
st.write(
        """
        - 💻 Programming: C, Python(keras, tensorflow, flask, numpy, tkinter), SQL.
        - 💨 Modelling: Linear Regression, Binary Classification, Multiclass Classification.
        - 🧬 Others: Colab, Jupyter Notebook, Github.
        """
)

# ---WORK HISTORY---
st.write("#")
st.subheader("Work History")
st.write("---")

# ---JOB1---
st.write("")
st.write("01/11/2023")
st.write("**Data Analyst Intern | Accenture**")
st.write(
        """
         - Advised a hypothetical client as a Data Analyst at Accenture.
         - Analyzed 7 datasets to inform strategic decisions.
         - Prepared a presentation for the client and stakeholders
        """
)

# ---JOB2---
st.write("#")
st.write("23/01/2023 - 31/03/2023")
st.write("**Research Intern | AI4ICPS, IIT Kharagpur**")
st.write(
        """
        - Analyzed research papers.
        - Problem analysis and team discussions.
        """
)

# ---PROJECTS & ACCOMPLISHMENTS---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")