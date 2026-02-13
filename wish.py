import streamlit as st

st.set_page_config(page_title="Valentine Surprise 💖", layout="centered")

# Title
st.title("🌹 A Valentine’s Day Surprise 🌹")
st.write("Click below to open your surprise!")

# Button logic
if "clicked" not in st.session_state:
    st.session_state.clicked = False

def reveal():
    st.session_state.clicked = True

if not st.session_state.clicked:
    st.button("🎁 Open Your Surprise", on_click=reveal)

if st.session_state.clicked:
    st.markdown("""
        <div style='text-align:center;'>
            <h1 style='font-size:4rem; color:#E91E63;'>Happy Valentine’s Day! 💕</h1>
            <p style='font-size:1.5rem;'>Wishing you love, laughter, and joy today and always!</p>
            <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="300"/>
        </div>
    """, unsafe_allow_html=True)

