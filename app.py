from pathlib import Path

import streamlit
import streamlit as st
from PIL import Image
import pandas as pd


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
interest in building a career in data."""

EMAIL = "animesh.maity.iam@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/animesh-maity",
    "Github": "https://github.com/animesh-am",
    "Hackerrank": "https://www.hackerrank.com/profile/animesh_maity_i1",
}

PROJECTS = {
    "🏆 Food Ordering Website": "http://moody-foody.zya.me/",
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

# Define the layout for social links
col1, col2, col3 = st.columns(3)

# Render LinkedIn icon with label and link
with col1:
    st.markdown('[<img width="60" height="60" src="https://img.icons8.com/color/480/linkedin.png" alt="linkedin"/>](https://linkedin.com/in/animesh-maity)', unsafe_allow_html=True)
    st.write("LinkedIn")

# Render Github icon with label and link
with col2:
    st.markdown('[<img width="60" height="60" src="https://img.icons8.com/windows/60/github.png" alt="github"/>](https://github.com/animesh-am)', unsafe_allow_html=True)
    st.write("Github")

# Render Hackerrank icon with label and link
with col3:
    st.markdown('[<img width="60" height="60" src="https://img.icons8.com/windows/32/hackerrank.png" alt="hackerrank"/>](https://www.hackerrank.com/profile/animesh_maity_i1)', unsafe_allow_html=True)
    st.write("Hackerrank")

# # Render LinkedIn icon using Icons8
# st.markdown('<img width="48" height="48" src="https://img.icons8.com/color/480/linkedin.png" alt="linkedin"/>', unsafe_allow_html=True)
# st.markdown('<img width="70" height="70" src="https://img.icons8.com/carbon-copy/100/github.png" alt="github"/>', unsafe_allow_html=True)
# st.markdown('<img width="60" height="60" src="https://img.icons8.com/windows/32/hackerrank.png" alt="hackerrank"/>', unsafe_allow_html=True)
#
#
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# ---EDUCATION DETAILS---
st.write("#")
st.subheader("Education Details")
st.write("---")

# Education details in tabular form
education_details = {
    "Degree": ["BCA (Bachelor of Computer Applications)", "ISC (Indian School Certificate)", "ICSE (Indian Certificate of Secondary Education)"],
    "University": ["Midnapore College (Autonomous)", "Contai Public School", "Contai Public School"],
    "Year": ["2024", "2021", "2019"],
    "Percentage": ["89.42%", "92.5%", "95%"],
}

# Education details in tabular form without serial numbers
education_df = pd.DataFrame(education_details)
st.markdown(education_df.style.hide(axis = "index").to_html(), unsafe_allow_html = True)


# ---EXPERIENCE & QUALIFICATIONS---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
        """
        - ✅ Basic Understanding about C and Python.
        - ✅ Basic Understanding in Convolution Neural Network and Deep Learning.
        - ✅ Worked as a team and analyzed Research Papers.
        - ✅ Advised a hypothetical client as a Data Analyst at Accenture in Virtual Internship.
        - ✅ Built several classifier and recognizer.
        """
)

# ---SKILLS---
st.write("#")
st.subheader("Hard Skills")
st.write(
        """
        - 💻 Programming: C, Python(keras, tensorflow, flask, numpy), C++, MySQL, PHP, Java.
        - 💨 Modelling: Linear Regression, Binary Classification, Multiclass Classification.
        - 👨‍💻 Web Development: HTML, CSS, Javascript
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
st.write("Sep 2023 - Sep 2023")
st.write("**Data Scientist Intern | CodeClause, Remote Internship**")
st.write(
        """
        - Built a predictor for loan approval.
        - Built a speech emotion recognizer.
        - Performed Data Analysis to generate result on Uber Dataset.
        """
)

# ---JOB3---
st.write("#")
st.write("Jan 2023 - Mar 2023")
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

# ---RESEARCH PROJECT---
st.write("#")
st.subheader("Research Project")
st.write("---")

# Research project details
st.write("**Groundnut Leaf Disease Classification**")
st.write("***Midnapore College (Autonomous)***")
st.write("- Comparative study of CNN architectures.")
st.write("- \tDeveloping a deep learning model for leaf disease classification.")
st.write("- Utilizing Python, Deep Learning, and Neural Networks.")



# ---HOBBIES---
st.write("#")
st.subheader("Hobbies")
st.write("---")

# Add hobbies
st.write("- ✏ Drawing")
st.write("- 🎈 Painting")
st.write("- 🏊‍♀️ Swimming")
st.write("- 🍳 Cooking")