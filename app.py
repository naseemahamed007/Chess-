# app.py

import streamlit as st
from data import tournaments

# Page Config
st.set_page_config(
    page_title="Nas Matrix Chess",
    layout="wide"
)

# Theme
st.markdown("""
<style>

body {
    background-color:#020617;
    color:white;
}

.stButton>button {
    background:#facc15;
    color:black;
    border-radius:10px;
    font-weight:bold;
    padding:10px;
}

.card {
    background:#020617;
    border:1px solid #1e293b;
    padding:20px;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style="text-align:center;">♟️ Nas Matrix Chess Association</h1>
<h4 style="text-align:center;color:gray;">
Official Tournament Platform
</h4>
""", unsafe_allow_html=True)

st.divider()

# Association Info
st.markdown("## 🏛️ About Association")

st.write("""
Nas Matrix Chess Association organizes professional chess tournaments,
training programs, and competitive events to build strong players
and strong character.
""")

st.divider()

# Tournament Section
st.markdown("## 🏆 Upcoming Tournaments")

cols = st.columns(3)

i = 0

for key, t in tournaments.items():

    with cols[i % 3]:

        st.markdown(f"""
        <div class="card">
        <h3>{t["title"]}</h3>
        <p>📅 {t["date"]}</p>
        <p>💰 {t["fee"]}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("View Details", key=key):

            st.session_state["tournament"] = key
            st.switch_page("pages/1_Tournament.py")

    i += 1

st.divider()

# Footer
st.markdown("""
<p style="text-align:center;color:gray;">
© 2026 Nas Matrix Chess | All Rights Reserved
</p>
""", unsafe_allow_html=True)
