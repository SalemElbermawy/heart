import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="INTRO PROJECT", page_icon="❤️", layout="wide")

def img_to_b64(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    suffix = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(suffix, "jpeg")
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/{mime};base64,{data}"

def resolve(src: str) -> str:
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return img_to_b64(src)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --primary:#dc2626;
    --primary-dark:#991b1b;
    --primary-light:#fecaca;
    --bg:#04191a;
    --surface:#0a2829;
    --border:rgba(220,38,38,0.25);
    --text:#f3f4f6;
    --muted:#9ca3af;
    --glow:rgba(220,38,38,0.18);
}

html, body, .stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 2rem 3rem 4rem !important;
    max-width: 1200px;
}

/* HERO */
.hero-wrapper {
    text-align: center;
    padding: 3rem 0 1.5rem;
    position: relative;
}

.hero-wrapper::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width: 600px;
    height: 180px;
    background: radial-gradient(ellipse, var(--glow) 0%, transparent 70%);
    pointer-events: none;
}

.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3rem,7vw,5.5rem);
    font-weight: 300;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    background: linear-gradient(135deg, var(--primary-light), var(--primary), var(--primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 0.85rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--muted);
}

.hero-divider {
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    margin: 1.4rem auto;
}

.banner-frame {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--border);
    box-shadow: 0 20px 80px rgba(0,0,0,0.7), 0 0 60px var(--glow);
    margin: 1.5rem 0 3rem;

    height: 420px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #04191a;
}

.banner-frame img {
    width: 100%;
    height: 100%;
    object-fit: contain; /*  */
}

/* SECTION */
.section-label {
    font-size: 0.72rem;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

.footer {
    text-align: center;
    margin-top: 4rem;
    font-size: 0.75rem;
    color: var(--muted);
    text-transform: uppercase;
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)

HERO_IMAGE = "banner.jpg"
hero_src = resolve(HERO_IMAGE)

st.markdown("""
<div class="hero-wrapper">
    <p class="hero-sub">✦ Welcome to ✦</p>
    <h1 class="hero-title">FLOW GUARD</h1>
    <div class="hero-divider"></div>
    <p class="hero-sub">Crafting tomorrow’s solutions</p>
</div>
""", unsafe_allow_html=True)

if hero_src:
    st.markdown(f"""
    <div class="banner-frame">
        <img src="{hero_src}">
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Banner image not found. Put 'banner.jpg' in the same folder.")


st.markdown('<div class="footer">© 2026 FLOW GUARD BIO TALENT</div>', unsafe_allow_html=True)