import re
import streamlit as st
import requests

WEBHOOK_URL = ""
def contect_form():

    with st.form("conteact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error(
                    "Email service is not set up. Please try again later.", icon= "📧"
                )
                st.stop()

            if not name:
                st.error("Please enter your name.", icon="😶‍🌫️")
                st.stop()
            
            if not email:
                st.error("Please provide your email address.", icon="📨")
                st.stop()                

            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📧")
                st.stop()
 
            if not message:
                st.error("Please provide a message...", icon="💬")
                st.stop()

            # Prepare the data payload and send it to the specified webhook url.
            data = {"email": email,"name":name, "message":message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Message sent successfully 🎉. Thank you!", icon="🚀")
            else:
                st.error("Failed to send the message. Please try again later.", icon="😨")