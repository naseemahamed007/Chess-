# tournament.py

import streamlit as st
from data import tournaments

st.set_page_config(page_title="Tournament Details")

# Safety
if "tournament" not in st.session_state:
    st.switch_page("app.py")

t = tournaments[st.session_state["tournament"]]

# Title
st.title("🏆 " + t["title"])

st.caption("Organized by " + t["organizer"])

st.divider()

# Info
st.write("📅 Date:", t["date"])
st.write("🌐 Mode:", t["mode"])
st.write("♟️ Platform:", t["platform"])
st.write("⚡ Format:", t["format"])
st.write("⏱️ Time Control:", t["time_control"])
st.write("💰 Entry Fee:", t["fee"])

st.divider()

# About
st.markdown("## 📖 About")
st.write(t["about"])

# Prizes
st.markdown("## 🏅 Prizes")

for p in t["prizes"]:
    st.write("•", p)

st.divider()

# Team
st.markdown("## 👥 Organizing Team")

for role, name in t["team"].items():
    st.write(f"**{role}:** {name}")

st.divider()

# Buttons
col1, col2 = st.columns(2)

with col1:

    if st.button("📝 Register Now"):
       st.switch_page("pages/2_Register.py")
with col2:

    if st.button("⬅️ Back to Home"):
        st.switch_page("app.py")
