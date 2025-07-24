
# Local LLM Chat App

## Overview
A simple real-time chat application built using **Streamlit** for the frontend, **FastAPI** as the backend, and **Ollama** running a local LLM (LLaMA 3 model) for natural language responses.

This project is part of SEQATO’s LLM Awareness and Portfolio Development Program.

---

## Tools & Tech

- [Streamlit](https://streamlit.io/) – Frontend UI for user interactions  
- [FastAPI](https://fastapi.tiangolo.com/) – Backend API service  
- [Ollama](https://ollama.com/) – Local LLM runtime (using the `llama3` model)  
- Python 3.8+  
- `uvicorn`, `requests`, `CORS middleware` for backend functionality

---

## Folder Structure

```
llm_chat_app/
├── backend/
│   └── main.py          # FastAPI backend logic
├── frontend/
│   └── app.py           # Streamlit frontend UI
├── requirements.txt     # Project dependencies
├── README.md            # Project instructions
```

---

##  How to Run the App

### Step 1: Install Python & Pip

Ensure Python 3.8+ is installed. Then install pip packages:

```bash
pip install -r requirements.txt
```

---

### Step 2: Set Up Ollama

Install [Ollama](https://ollama.com) for your OS and start the local model:

```bash
ollama pull llama3
ollama run llama3
```

This will start the LLM server at: `http://localhost:11434`

---

### Step 3: Run the FastAPI Backend

Navigate to the `backend` folder and start the API service:

```bash
cd backend
uvicorn main:app --reload --port 8000
```

Backend will be live at: `http://localhost:8000/chat`

---

### Step 4: Run the Streamlit Frontend

In a separate terminal, navigate to the `frontend` folder and start the Streamlit app:

```bash
cd frontend
streamlit run app.py
```

Frontend will open at: `http://localhost:8501`

---

## Example Workflow

1. Enter a message in the chat input box.
2. FastAPI sends the message to Ollama (LLaMA 3 model).
3. Ollama generates a response and returns it.
4. Streamlit displays the assistant's reply in real time.

---

## Sample Request Flow

```
[User Input] → Streamlit UI → FastAPI Endpoint → Ollama Model → Response → Streamlit Display
```

---

## requirements.txt

```txt
streamlit
fastapi
uvicorn
requests
```

---

## Demo Screenshot

> Add a screenshot of your UI here once available:
```
![Local LLM Chat App UI](screenshot.png)
```

---

## Tips

- You can swap `llama3` with other models supported by Ollama (e.g., `llama2`, `gemma`, `phi`).
- Ensure ports `8000` (FastAPI) and `11434` (Ollama) are not blocked or used by other services.
- Optional: Use `ngrok` or similar tools to expose for demo purposes.

---

## Contributing

This project is part of SEQATO’s internal LLM skill-building initiative. Contributions from team members in terms of enhancements or alternate UIs are welcome.

---

## License

This is a learning project. All usage is internal to SEQATO unless otherwise specified.
