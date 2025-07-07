import streamlit as st
import requests
import json

st.set_page_config(page_title="SeqBot - Local LLM Chat", layout="centered")

# Initialize session
if "history" not in st.session_state:
    st.session_state.history = []
if "pending_input" not in st.session_state:
    st.session_state.pending_input = None

# Style
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0e1117;
            color: #c9d1d9;
        }
        .chat-container {
            margin-top: 1rem;
            padding: 0 1rem 6rem 1rem;
            max-height: 70vh;
            overflow-y: auto;
        }
        .chat-message {
            border-radius: 10px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 80%;
            word-wrap: break-word;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }
        .user {
            background-color: #2d333b;
            align-self: flex-end;
            margin-left: auto;
        }
        .bot {
            background-color: #3a3f4b;
            align-self: flex-start;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h2 style='text-align: center; color: #d0d0d0;'>🤖 SeqBot — Your Local LLM Assistant</h2>", unsafe_allow_html=True)

# --- Add "You:" message BEFORE streaming
if st.session_state.pending_input:
    prompt = st.session_state.pending_input
    st.session_state.pending_input = None
    st.session_state.history.append(("You", prompt))
    st.rerun()  # Immediately rerun to show "You:" in UI

# Display chat history (except last "pending" reply)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.history:
    if sender == "SeqBot" and message == "__STREAMING__":
        continue  # Placeholder, will be handled separately
    css_class = "user" if sender == "You" else "bot"
    st.markdown(f"""
        <div class="chat-message {css_class}">
            <div><strong>{sender}:</strong><br>{message}</div>
        </div>
    """, unsafe_allow_html=True)

# Stream reply if last was "You"
if st.session_state.history and st.session_state.history[-1][0] == "You":
    # Add temp marker to track streaming
    st.session_state.history.append(("SeqBot", "__STREAMING__"))
    bot_placeholder = st.empty()
    full_response = ""

    prompt = st.session_state.history[-2][1]
    try:
        with requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": True},
            stream=True,
        ) as resp:
            for line in resp.iter_lines():
                if line:
                    data = json.loads(line.decode('utf-8'))
                    token = data.get("response", "")
                    full_response += token
                    bot_placeholder.markdown(f"""
                        <div class="chat-message bot">
                            <div><strong>SeqBot:</strong><br>{full_response}</div>
                        </div>
                    """, unsafe_allow_html=True)
    except Exception as e:
        full_response = f"⚠️ Error: {e}"

    # Replace temp marker with actual response
    st.session_state.history[-1] = ("SeqBot", full_response.strip())
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.pending_input = user_input
    st.rerun()
