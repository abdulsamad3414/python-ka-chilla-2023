import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


# # Web app title
# st.markdown(""" # **Exploratory Data Analysis web Application* 
#             This app create by Samad Called EDA APP""")
# with st.sidebar.header("upload your dataset(.csv)"):
#     upload_file =st.sidebar.file_uploader("Upload your file", type=["csv"])
#     df =sns.load_dataset("titanic")
#     st.sidebar.markdown("sample dataset")
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("Business Inquiry Form")

# Form inputs
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit")

if submit:
    if name and email and message:
        # Email configuration
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"  # Use app password, not your main password
        receiver_email = "your_email@gmail.com"

        subject = f"New Inquiry from {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Send email via Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            st.success("Your message has been sent successfully!")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.warning("Please fill in all required fields.")

    # Clear form inputs
    name = ""
    email = ""
    phone = ""
    message = ""
