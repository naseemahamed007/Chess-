import streamlit as st

# Page Settings
st.set_page_config(
    page_title="Chennai Open Chess Tournament",
    layout="wide"
)

# Google Form Link
FORM_URL = "https://forms.gle/eX3hB9CLruzJpLk26"


# Title
st.markdown("""
<h1 style="text-align:center; color:#1f3c88;">
🏆 Chennai Open Chess Tournament ♟️
</h1>

<h3 style="text-align:center; color:gray;">
Organized by Nas Matrix Chess
</h3>
""", unsafe_allow_html=True)

st.divider()

# Info Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📅 Tournament Details")
    st.write("🗓️ Date: 28 March 2026")
    st.write("🌐 Mode: Online")
    st.write("♟️ Platform: Chess.com")
    st.write("⚡ Format: Rapid | Swiss System")
    st.write("⏱️ Time Control: 10 Minutes")

with col2:
    st.markdown("### 💰 Fees & Awards")
    st.write("💵 Entry Fee: ₹150")
    st.write("🏅 Medal: All Participants")
    st.write("📜 Certificate: All Players")
    st.write("🏆 Trophies: Winner & Runner-up")

st.divider()

# About
st.markdown("## 📖 About Tournament")

st.write("""
The Chennai Open Chess Tournament is a professionally organized
online competition that promotes discipline, fair play,
and competitive excellence.

All players will receive official certificates and recognition.
""")

st.divider()

# Organizing Team
st.markdown("## 👤 Organizing Team")

st.markdown("""
### 🌟 Leadership & Management

**Naseem Ahamed**  
Arena International Master (AIM)  
Director – Nas Matrix Chess  

---

### 📋 Tournament Organizer

**Omer Kose**  
Chief Organizer  

---

### 📢 Media & Promotions

**Abuzer**  
Media Head  
""")

st.divider()

# Contact
# Contact
st.markdown("## 📞 Contact & Social Media")

st.write("📱 WhatsApp: 7094602011")
st.write("📧 Email: naseemishere0@gmail.com")

st.markdown(
    """
    📸 Instagram: 
    <a href="https://instagram.com/nasmatrixchess" target="_blank">
    @nasmatrixchess
    </a>
    """,
    unsafe_allow_html=True
)

st.divider()

# Register Button (Direct Google Form)

# Register Button (Safe Link)
# Register Button (Safe Link)

colA, colB, colC = st.columns([1, 2, 1])  # <-- This creates colB

with colB:
    st.link_button(
        "📝 REGISTER NOW",
        "https://forms.gle/eX3hB9CLruzJpLk26",
        use_container_width=True
    )

st.divider()

# Footer
st.markdown("""
<hr>
<p style="text-align:center; color:gray;">
© 2026 Nas Matrix Chess | All Rights Reserved
</p>
""", unsafe_allow_html=True)
