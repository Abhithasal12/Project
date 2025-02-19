import streamlit as st

#--- PAGE SETUP ---

about_page = st.Page(
    page="view/aboutMe.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

projects_1_page = st.Page(
    page="view/sales_dashboard.py",
    title="sales dashboard",
    icon=":material/bar_chart:",
)

projects_2_page = st.Page(
    page="view/chatbot.py",
    title="chat bot",
    icon=":material/smart_toy:",
)

#---NAVIGATION SETUP(without section)---
#pg= st.navigation(pages=[about_page, projects_1_page,projects_2_page])

#---NAVIGATION SETUP(with section)---

pg = st.navigation(
    {
        "Info": [about_page],
        "Project":[projects_1_page,projects_2_page],
    }
)
#----SHARED ALL PAGES---

st.logo("Assets/png.png")
# st.sidebar.text("Made with 💝 by seven")


pg.run()