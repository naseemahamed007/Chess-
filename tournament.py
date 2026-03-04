import streamlit as st
from data import tournaments

st.set_page_config(page_title="Tournament Details")

if "tournament" not in st.session_state:
    st.switch_page("app.py")

t = tournaments[st.session_state["tournament"]]

st.title("🏆 " + t["name"])

st.divider()

st.write("📅 Date:", t["date"])
st.write("🌐 Mode:", t["mode"])
st.write("♟️ Platform:", t["platform"])
st.write("💰 Fee:", t["fee"])
st.write("⏱️ Time:", t["time"])
st.write("🏅 Prize:", t["prize"])

st.divider()

st.markdown("### 📖 About")
st.write(t["about"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Register Now"):
        st.switch_page("register.py")

with col2:
    if st.button("⬅️ Back"):
        st.switch_page("app.py")
