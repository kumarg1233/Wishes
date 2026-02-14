import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Valentine Surprise 💖", layout="centered")

# --- CSS styling ---
st.markdown("""
<style>
body { background: #fff5f8; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.main-heading { font-weight: 900; font-size: 2.8rem; text-align: center; color: #222; margin-top: 2rem; margin-bottom: 1rem; }
.main-heading span { margin: 0 10px; color: #e91e63; font-size: 2.8rem; vertical-align: middle; }
.subheading { font-size: 1.3rem; font-weight: 600; color: #ff4b4b; text-align: center; margin-bottom: 2rem; }

div.stButton > button {
    background: linear-gradient(90deg, #ff6ec4 0%, #7873f5 100%) !important;
    color: white !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    padding: 14px 48px !important;
    border-radius: 30px !important;
    cursor: pointer !important;
    box-shadow: 0 6px 15px rgba(255,110,196,0.5) !important;
    transition: all 0.3s ease !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    border: none !important;
}
div.stButton > button:hover { box-shadow: 0 10px 25px rgba(255,110,196,0.7) !important; transform: translateY(-4px) !important; }

.surprise-content { text-align: center; margin-top: 2rem; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.surprise-content h1 { font-size: 3.8rem; color: #e91e63; margin-bottom: 0.5rem; animation: pulse 2s infinite; }
.surprise-content p { font-size: 1.4rem; margin-bottom: 1.5rem; color: #333; animation: pulse 2.5s infinite; }

/* Container for teddies + AG logo */
.teddy-ag-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
    margin-top: 30px;
    margin-bottom: 30px;
    animation: float 3s ease-in-out infinite;
}
.teddy-img { width: 150px; height: 150px; object-fit: contain; animation: pulse 2s infinite; }
.ag-logo { width: 160px; height: 160px; object-fit: cover; border-radius: 20px; animation: pulse 1.5s infinite; }

/* Centered Valentine GIF */
.valentine-gif-container {
    text-align: center;
    margin: 20px 0;
    animation: float 4s ease-in-out infinite;
}
.valentine-gif {
    width: 500px;
    height: auto;
    border-radius: 10px;
}

/* Keyframes */
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}
.surprise-content p {
    color: #FF7449; /* yellow-orange color */
    font-size: 1.3rem;
}
</style>
""", unsafe_allow_html=True)

# --- Main heading ---
st.markdown("""
<div class="main-heading" style="color: #FF446E;">
    <span>🌹</span> A Valentine’s Day Surprise <span>🌹</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="subheading">Click below to open  surprise!</div>', unsafe_allow_html=True)

# --- Session state ---
if "clicked" not in st.session_state:
    st.session_state.clicked = False

def reveal():
    st.session_state.clicked = True

# --- Button ---
if not st.session_state.clicked:
    st.markdown('<div style="display:flex; justify-content:center;">', unsafe_allow_html=True)
    if st.button("🎁 Open Your Surprise", on_click=reveal):
        pass
    st.markdown('</div>', unsafe_allow_html=True)

# --- Surprise content ---
if st.session_state.clicked:
    st.markdown("""
    <div class="surprise-content">
        <h1>Happy Valentine’s Day! 💕</h1>
        <p>Wishing you love, laughter, and joy today and always!</p>
    </div>
    """, unsafe_allow_html=True)

    # Load local images
    left_teddy = Image.open("teddy.png")    # Left teddy
    right_teddy = Image.open("teddy.png")   # Right teddy
    ag_logo = Image.open("vale.png")         # AG logo
    valentine_gif = Image.open("AG.png")    # Local Valentine GIF

    
    
    # Convert AG logo to base64
    buffered = BytesIO()
    ag_logo.save(buffered, format="PNG")
    ag_logo_b64 = base64.b64encode(buffered.getvalue()).decode()

    # Convert Valentine GIF to base64
    buffered_gif = BytesIO()
    valentine_gif.save(buffered_gif, format="GIF")
    gif_b64 = base64.b64encode(buffered_gif.getvalue()).decode()

    buffered = BytesIO()
    right_teddy.save(buffered, format="PNG")
    r_teddy_b64 = base64.b64encode(buffered.getvalue()).decode()
    
    buffered = BytesIO()
    left_teddy.save(buffered, format="PNG")
    l_teddy_b64 = base64.b64encode(buffered.getvalue()).decode()
    
    # Display Valentine GIF below
    st.markdown(f"""
    <div class="valentine-gif-container">
        <img src="data:image/gif;base64,{gif_b64}" class="valentine-gif"/>
    </div>
    """, unsafe_allow_html=True)

    
    # Display teddies + AG logo
    st.markdown(f"""
    <div class="teddy-ag-container">
        <img src="data:image/png;base64, {l_teddy_b64}" class="teddy-img"/>
        <img src="data:image/png;base64,{ag_logo_b64}" class="ag-logo"/>
        <img src="data:image/png;base64, {r_teddy_b64}" class="teddy-img"/>
    </div>
    """, unsafe_allow_html=True)

    
