import streamlit as st
from datetime import datetime
import google.generativeai as genai

st.set_page_config(
    page_title="AI Chat Bot",
    layout="wide",
    initial_sidebar_state="auto"
)


def generate_response(user_text: str) -> str:
    try:
        key = "Enter Your API Key from Gemini"
        genai.configure(api_key=key)

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_text)

        return response.text.strip()

    except Exception as e:
        return "Error: " + str(e)

def init_state():
    if "conversations" not in st.session_state:
        st.session_state.conversations = {}
    if "current_chat" not in st.session_state:
        create_new_chat()

def create_new_chat():
    next_num = len(st.session_state.conversations) + 1
    chat_id = f"Chat {next_num}"
    st.session_state.conversations[chat_id] = []
    st.session_state.current_chat = chat_id

def format_timestamp(ts: datetime) -> str:
    return ts.strftime("%Y-%m-%d %H:%M:%S")


init_state()


with st.sidebar:
    st.header("Conversations")

    chat_ids = list(st.session_state.conversations.keys())
    if chat_ids:
        selected = st.radio(
            "Select chat",
            chat_ids,
            index=chat_ids.index(st.session_state.current_chat)
        )
        st.session_state.current_chat = selected

    st.markdown("---")

    if st.button("New Chat"):
        create_new_chat()
        st.rerun()

    st.markdown("---")
    st.caption("AI Chat Bot — Made by Tarun")

st.title("AI Chat Bot")

current_chat = st.session_state.current_chat
messages = st.session_state.conversations[current_chat]

st.subheader(f"Conversation: {current_chat}")

for idx, msg in enumerate(messages, start=1):
    role = msg["role"]
    text = msg["content"]
    ts = msg["timestamp"]
    ts_str = format_timestamp(ts)

    safe_text = (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br>")
    )

    if role == "user":
        align = "right"
        bubble_style = (
            "display:inline-block;"
            "padding:12px 18px;"
            "border-radius:14px;"
            "max-width:75%;"
            "background: linear-gradient(135deg, #A855F7, #7C3AED);"
            "color:white;"
            "box-shadow: 0 4px 10px rgba(0,0,0,0.12);"
        )
        label = f"User {idx}"
    else:
        align = "left"
        bubble_style = (
            "display:inline-block;"
            "padding:12px 18px;"
            "border-radius:14px;"
            "max-width:75%;"
            "background: linear-gradient(135deg, #3B82F6, #1E40AF);"
            "color:white;"
            "box-shadow: 0 4px 10px rgba(0,0,0,0.12);"
        )
        label = f"AI {idx}"

    st.markdown(
        f"""
        <div style="text-align:{align}; margin:10px 0;">
            <div style="{bubble_style}">
                <strong>{label}</strong><br>
                {safe_text}
                <div style="font-size:10px; opacity:0.8; margin-top:6px;">{ts_str}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

with st.form(key="chat_form", clear_on_submit=True):
    user_text = st.text_area("Your message", height=80)
    submitted = st.form_submit_button("Send")

if submitted and user_text.strip():
    messages.append({
        "role": "user",
        "content": user_text.strip(),
        "timestamp": datetime.now()
    })

    reply_text = generate_response(user_text.strip())

    messages.append({
        "role": "bot",
        "content": reply_text,
        "timestamp": datetime.now()
    })

    st.session_state.conversations[current_chat] = messages
    st.rerun()
