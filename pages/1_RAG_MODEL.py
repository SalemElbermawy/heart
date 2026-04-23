import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from rag_system import response

st.set_page_config(page_title="FlowGuard AI", page_icon="🩸", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --primary:      #dc2626;
    --primary-dark: #991b1b;
    --primary-light:#fecaca;
    --glow:         rgba(220,38,38,0.15);

    --bg:          #04191a;
    --surface2:    #0a2829;
    --border:      rgba(220,38,38,0.22);
    --text:        #d6f5f3;
    --muted:       #9ca3af;
}

html, body, [class*="css"], .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 3rem !important; max-width: 820px; }

section[data-testid="stSidebar"] {
    background: var(--bg) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

.topbar {
    text-align: center;
    padding: 2rem 0 1.5rem;
    position: relative;
    margin-bottom: 1rem;
}
.topbar::before {
    content: '';
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    width: 400px; height: 120px;
    background: radial-gradient(ellipse, var(--glow) 0%, transparent 70%);
}
.topbar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    letter-spacing: 0.22em;
    background: linear-gradient(135deg, var(--primary-light), var(--primary), var(--primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.topbar-sub {
    font-size: 0.68rem;
    letter-spacing: 0.3em;
    color: var(--muted);
}
.topbar-line {
    width: 50px; height: 1.5px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    margin: 0.8rem auto 0;
}

.chat-wrap {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.msg-row { display: flex; gap: 0.7rem; align-items: flex-end; }
.msg-row.user { flex-direction: row-reverse; }

.avatar {
    width: 34px; height: 34px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    border: 1px solid var(--border);
}
.avatar.bot { background: var(--surface2); color: var(--primary); }
.avatar.user { background: var(--primary-dark); }

.bubble {
    max-width: 74%;
    padding: 0.8rem 1.1rem;
    border-radius: 16px;
    font-size: 0.92rem;
}
.bubble.bot {
    background: var(--surface2);
    border: 1px solid var(--border);
}
.bubble.user {
    background: rgba(220,38,38,0.1);
    border: 1px solid rgba(220,38,38,0.3);
}

.input-row {
    display: flex;
    align-items: center;
    gap: 8px;
}

div[data-testid="stTextInput"] input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    transition: all 0.2s ease;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px var(--glow) !important;
    transform: scale(1.01);
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, var(--primary-dark), var(--primary)) !important;
    color: white !important;
    border-radius: 50% !important;
    width: 42px !important;
    height: 42px !important;
    padding: 0 !important;
    font-size: 1rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stFormSubmitButton"] button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 10px var(--glow);
}
div[data-testid="stFormSubmitButton"] button:active {
    transform: scale(0.95);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <h1 class="topbar-title">🩸 FlowGuard AI</h1>
    <p class="topbar-sub">Clot Risk Assistant</p>
    <div class="topbar-line"></div>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form("chat_form", clear_on_submit=True):
    st.markdown('<div class="input-row">', unsafe_allow_html=True)

    col1, col2 = st.columns([6, 1])

    with col1:
        user_input = st.text_input(
            "",
            placeholder="Ask about clot risk or your data...",
            label_visibility="collapsed"
        )

    with col2:
        submitted = st.form_submit_button("➤")

    st.markdown('</div>', unsafe_allow_html=True)

if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.spinner("Thinking..."):
        bot_reply = response(user_input)
    st.session_state.messages.append({"role": "bot", "text": bot_reply})
    st.rerun()


if st.session_state.messages:

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

    for msg in st.session_state.messages:
        role = msg["role"]
        text = msg["text"]

        avatar = "🩺" if role == "bot" else "🧑"

        if role == "user":
            st.markdown(f"""
            <div class="msg-row user">
                <div class="avatar user">{avatar}</div>
                <div class="bubble user">{text}</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="msg-row bot">
                <div class="avatar bot">{avatar}</div>
                <div class="bubble bot">{text}</div>
            </div>
            """, unsafe_allow_html=True)

else:
    st.info("Start by asking about clot risk, blood flow, or your model.")