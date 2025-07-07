
# 📘 SEQATO LLM Awareness and Portfolio Development Program — Learning Log

## 🧠 Phase 1: Local LLM Chat App

### 🗓️ Progress Summary

| Date | Activity | Notes / Challenges / Fixes |
|------|----------|-----------------------------|
| **June 30, 2025** | Kickoff | Started building the Local LLM Chat App using **Streamlit**, **FastAPI**, and **Ollama**. Set up `llm_chat_app` directory structure. |
| **July 1–2, 2025** | Basic UI Setup | Created initial chat layout with Streamlit. Used `text_input()` and `button()` layout. |
|  | **Challenges:** Clear Chat button placement and response alignment were off. |
|  | **Fix:** Switched to `st.chat_input()` and rewired `st.session_state` for better UX. |
| **July 3, 2025** | Improved UI Design | Redesigned chat to look like ChatGPT. Used custom CSS for dark theme, message bubbles, and aligned "user" and "bot" messages. |
|  | Added Send/Clear Chat buttons. Implemented footer and spacing improvements. |
| **July 4, 2025** | Response Fix | Fixed issue where user’s first message required a second message to trigger a bot response. Used `pending_input` logic and session rerun to process immediately. |
| **July 5, 2025** | Final UI Alignment | Aligned Clear Chat button next to the input. Removed unnecessary headers and placeholder lines. Achieved smooth and clean chat UI. |
| **July 6, 2025** | ✅ Streaming Reply | Implemented token-by-token streaming using `requests.post(..., stream=True)` with Ollama. Added logic to render responses in real-time using `st.empty()` placeholder. |
|  | **Challenge:** User message was not visible immediately. |
|  | **Fix:** Stored "You" message right before streaming starts and re-rendered immediately. |
| **July 7, 2025** | Typing Animation | Added `"SeqBot is typing..."` placeholder before streaming begins. Handled this using a `("SeqBot", "typing...")` placeholder in session history and replaced after full response. |
|  | Final UI confirmed ✅ — streaming, input box at bottom, dark theme, polished layout |

---

### ✅ Tools & Skills Gained

- **Streamlit** – `st.chat_input`, layout handling, `session_state`, custom HTML/CSS
- **Ollama** – Local LLM API integration, streaming tokens
- **FastAPI (planned backend)** – Architecture understanding
- **Frontend polish** – Mimicked ChatGPT UI, real-time interaction
- **Debugging skills** – Handled widget state issues, stream delays, UI reruns

---
