import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Tournament Registration",
    layout="centered"
)

st.title("📝 Player Registration")

st.write("Fill the form carefully. All details must be correct.")

# Input Fields
name = st.text_input("Full Name")
username = st.text_input("Chess.com Username")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
age = st.number_input("Age", min_value=5, max_value=100)

st.divider()

# File name
file_name = "players_data.csv"

# Submit Button
if st.button("✅ Submit Registration"):

    if name and username and email and phone:

        data = {
            "Name": name,
            "Username": username,
            "Email": email,
            "Phone": phone,
            "Age": age,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        df_new = pd.DataFrame([data])

        # If file exists → append
        if os.path.exists(file_name):
            df_old = pd.read_csv(file_name)
            df_all = pd.concat([df_old, df_new], ignore_index=True)
            df_all.to_csv(file_name, index=False)

        # If file not exists → create
        else:
            df_new.to_csv(file_name, index=False)

        st.success("🎉 Registration Successful!")
        st.balloons()

    else:
        st.warning("⚠️ Please fill all fields correctly.")

st.divider()

# Back Button
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")
