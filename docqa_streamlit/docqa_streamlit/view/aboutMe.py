import streamlit as st
from forms.contact import contect_form
@st.dialog("Conteact Me")
#@st.experimental_dialog is end in 01-01-2025 is not working. (this is work(st.dialog())

def show_conteact_form():
    contect_form()
#----Hero SECTION---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)
with col2:
    st.title("Abhishek Thasal",anchor=False) 
    st.write(
        "Full Stack Developer and Data scientist with Generative AI    "
    )   
    if st.button("✉️ Conteact me"):
        show_conteact_form()

#---EXPERIENCE QUALIFICTIONS------
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 1 & 7 months years of experience actionable insights from data
    - strong hands on experience and knowledge in python and Excel
    - Bachelor degree in Financial market
    - completing my Full Stack Developer and Data scientist with Generative AI from INeuron
    - Excellent team-player and displaying a strong of initiative on tasks   
    """
)

#---SKILLS SECTION---

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming: Python, SQL
    - Data Visualization: MS Excel
    - Modeling: Logistic regression, linear regression
    - Database: MySQL, MongoDB
    """
)
