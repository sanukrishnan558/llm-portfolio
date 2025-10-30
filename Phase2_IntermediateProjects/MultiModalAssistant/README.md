# 🎯 Multimodal Assistant

An interactive AI assistant built with **Streamlit** that can understand text, images, and documents. It uses **Ollama**, **OpenAI**, or **Gemini** models for multimodal reasoning — allowing you to chat about uploaded images or documents.

---

## 🚀 Features

✅ **Multimodal Inputs** — Chat with text, images, and documents  
✅ **Model Flexibility** — Supports Ollama, OpenAI, or Gemini  
✅ **Streaming Responses** — Token-by-token response rendering for real-time feel  
✅ **Collapsible Settings Panel** — Cleaner UI design  
✅ **Image & Document Preview** — Uploaded files preview instantly  
✅ **Debug Mode** — Optional expander for seeing backend JSON & metadata

---

## 🧩 Project Structure

```
multimodal-assistant/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── assets/                # Optional folder for icons, images, etc.
```

---

## ⚙️ Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/multimodal-assistant.git
cd multimodal-assistant
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 Usage

### Run the app locally
```bash
streamlit run app.py
```

Then open the app in your browser — it’ll usually be available at:  
👉 **http://localhost:8501**

---

## ⚙️ Environment Variables

You can set API keys in a `.env` file or Streamlit secrets.

```bash
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

---

## 🧠 Example Interaction

**User:** *“What’s happening in this image?”*  
**Assistant:** *(Analyzes the uploaded image and responds with description or reasoning.)*

---

## 🧩 Technologies Used

- **Python 3.9+**
- **Streamlit** — Frontend UI
- **OpenAI / Gemini / Ollama** — Model integration
- **Pillow / PyPDF2** — For handling images and PDFs

---

## 🌟 Credits

Built by **Sanu Krishnan** as part of a personal AI project portfolio.

---

## 📜 License

MIT License © 2025 Sanu Krishnan
