import streamlit as st
from data import tournaments

st.set_page_config(
    page_title="Nas Matrix Chess",
    layout="wide"
)

# Theme
st.markdown("""
<style>
body {
    background-color:#0f172a;
    color:white;
}
.stButton>button {
    background:gold;
    color:black;
    border-radius:8px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style="text-align:center;">♟️ Nas Matrix Chess Association</h1>
<h4 style="text-align:center;color:gray;">Official Tournament Platform</h4>
""", unsafe_allow_html=True)

st.divider()

# Association Info
st.markdown("## 🏛️ Association Details")

st.write("""
Nas Matrix Chess promotes competitive excellence, discipline,
and professional tournament management.
""")

st.divider()

# Tournaments Section
st.markdown("## 🏆 Upcoming Tournaments")

cols = st.columns(3)

i = 0
for key, t in tournaments.items():

    with cols[i % 3]:

        st.subheader(t["name"])
        st.write("📅", t["date"])
        st.write("💰", t["fee"])

        if st.button("View Details", key=key):

            st.session_state["tournament"] = key
            st.switch_page("tournament.py")

    i += 1

st.divider()

# Footer
st.markdown("""
<p style="text-align:center;color:gray;">
© 2026 Nas Matrix Chess
</p>
""", unsafe_allow_html=True)
