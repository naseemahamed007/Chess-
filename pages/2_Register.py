# register.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os
from data import tournaments

st.set_page_config(page_title="Registration")

# Safety
if "tournament" not in st.session_state:
    st.switch_page("app.py")

t = tournaments[st.session_state["tournament"]]

# Title
st.title("📝 Tournament Registration")

st.subheader(t["title"])

st.divider()

# Form
with st.form("registration_form"):

    name = st.text_input("Full Name *")
    chess_id = st.text_input("Chess.com Username *")
    phone = st.text_input("Phone Number *")
    email = st.text_input("Email")
    age = st.number_input("Age", 5, 100)

    submit = st.form_submit_button("✅ Submit Registration")

# File per tournament
FILE = f"registrations_{st.session_state['tournament']}.csv"

# Save
if submit:

    if name and chess_id and phone:

        data = {
            "Tournament": t["title"],
            "Name": name,
            "Chess ID": chess_id,
            "Phone": phone,
            "Email": email,
            "Age": age,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        df_new = pd.DataFrame([data])

        if os.path.exists(FILE):

            df_old = pd.read_csv(FILE)
            df_all = pd.concat([df_old, df_new])
            df_all.to_csv(FILE, index=False)

        else:

            df_new.to_csv(FILE, index=False)

        st.success("🎉 Registration Successful!")
        st.balloons()

    else:

        st.error("⚠️ Please fill all required fields")

st.divider()

# Back
if st.button("⬅️ Back"):
    st.switch_page("pages/1_Tournament.py")
