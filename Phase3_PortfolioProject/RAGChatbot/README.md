# 🧠 Custom Chatbot Q&A (RAG Application)

A **Retrieval-Augmented Generation (RAG)** chatbot built using **LangChain**, **ChromaDB**, and **Ollama**.  
It allows users to upload documents (PDF/TXT) and ask contextual questions based on the content.

---

## 🚀 Features

- Document ingestion with **LangChain Document Loaders**
- Vector storage with **ChromaDB**
- Embedding using **HuggingFace MiniLM**
- Local LLM inference using **Ollama (Llama 2 / Mistral / Gemma)**  
- Interactive **Streamlit UI** for chat-based Q&A  
- Persistent chat memory for follow-up questions

---

## 📁 Folder Structure

```
RAGChatbot/
│
├── app.py               # Streamlit app for the chatbot UI
├── ingest.py            # Script to process and store document embeddings
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── data/                # Folder to store PDF/TXT documents
└── chroma_db/           # Chroma database for vector embeddings
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/sanukrishnan558/llm-portfolio.git
cd llm-portfolio/Phase3_PortfolioProject/RAGChatbot

# Create virtual environment
python -m venv .venv
.\.venv\Scriptsctivate    # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

---

## 🧩 Usage

### Step 1: Ingest documents
Place your `.pdf` or `.txt` files inside the `data/` folder, then run:
```bash
python ingest.py
```

### Step 2: Run the chatbot app
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🤖 Model Configuration (Ollama)

Ensure **Ollama** is installed and running locally.  
You can pull a model like **Llama 2** using:

```bash
ollama pull llama2
```

In `app.py`, you can change the model like this:

```python
llm = Ollama(model="mistral", temperature=0)
```

---

## 🧾 Example Questions

- “Summarize this document.”  
- “What are the key points mentioned about data security?”  
- “Who are the main stakeholders described?”

---

## 📜 License

MIT License © 2025 [Sanu Krishnan](https://github.com/sanukrishnan558)
