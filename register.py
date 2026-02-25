import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Tournament Registration")

st.title("📝 Chess Tournament Registration")

st.write("Fill the form to register for the tournament.")

st.divider()

# Form
with st.form("registration_form"):

    name = st.text_input("Full Name *")
    chess_id = st.text_input("Chess.com Username *")
    phone = st.text_input("Phone Number *")
    email = st.text_input("Email Address")
    age = st.number_input("Age", 5, 100)

    submit = st.form_submit_button("✅ Register")

# File name
FILE = "registrations.csv"

# When submitted
if submit:

    if name and chess_id and phone:

        data = {
            "Name": name,
            "Chess ID": chess_id,
            "Phone": phone,
            "Email": email,
            "Age": age,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        df_new = pd.DataFrame([data])

        # Save to file
        if os.path.exists(FILE):
            df_old = pd.read_csv(FILE)
            df_all = pd.concat([df_old, df_new], ignore_index=True)
            df_all.to_csv(FILE, index=False)
        else:
            df_new.to_csv(FILE, index=False)

        st.success("🎉 Registration Successful!")
        st.balloons()

    else:
        st.error("⚠️ Please fill all required fields (*)")

st.divider()

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")
