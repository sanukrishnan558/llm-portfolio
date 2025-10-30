# 🧠 Multimodal Assistant

The **Multimodal Assistant** is an AI-powered web application built with **Streamlit**, combining **text and image understanding**.  
It uses **Ollama’s LLaMA 3** model for natural language reasoning, along with **OCR and image captioning** for visual comprehension, and **FAISS** for context retrieval.

---

## 🚀 Features

- 🖼️ **Image Understanding** – Upload an image and extract captions + OCR text.  
- 💬 **Question Answering** – Ask questions related to the image or text context.  
- 🔎 **Document Retrieval** – Retrieves related documents using FAISS for grounded answers.  
- ⚡ **Streaming Responses** – LLM answers stream token-by-token for a real-time chat experience.  
- 🧩 **Clean UI** – Two-column layout with collapsible settings and document previews.

---

## 🧱 Project Structure

```
multimodal-assistant/
├── app.py               # Streamlit web app
├── llm_client.py        # LLM client using Ollama API
├── image_utils.py       # Image captioning & OCR logic
├── retriever.py         # FAISS retriever logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧰 Requirements

- Python 3.10+
- Ollama (with `llama3` model pulled)
- Streamlit
- Pillow
- FAISS
- pytesseract (for OCR)

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Run the App

1. Start your Ollama server:
   ```bash
   ollama serve
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Then open your browser at **http://localhost:8501** 🎉

---

## 🧠 How It Works

1. Upload an image → the app runs captioning + OCR.
2. Ask a question → it retrieves relevant text context from FAISS.
3. The **LLaMA 3** model combines image + text context to generate an intelligent answer.
4. The response is streamed token-by-token for smooth interactivity.

---

## 📦 Example Use Cases

- Visual question answering  
- Knowledge-based assistants using documents  
- Multimodal content summarization  
- AI research or LLM demo showcase  

---

## 🧑‍💻 Author

Developed by **Sanu Krishnan**  
Part of the **LLM Portfolio Project Series — SEQATO**

---

## 🪪 License

MIT License © 2025
