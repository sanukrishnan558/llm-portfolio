# 📰 News Topic Tracker

A **Streamlit** app to fetch top news headlines by category from the **GNews API** and summarize them using **Hugging Face Transformers** or **Ollama (LLaMA3)**.

---

## 🚀 Features
- **Choose news category** (e.g., World, Business, Technology, Sports, etc.)
- **Fetch top headlines** from GNews API
- **Summarize** each article using:
  - Hugging Face Transformers (local or API)
  - Ollama (LLaMA3 model)
- Direct **links to full articles**
- Lightweight, **interactive UI** via Streamlit

---

## 📂 Project Structure

NewsTopicTracker/
│
├── app.py # Main Streamlit app
├── news_scraper.py # News fetching logic (GNews API / RSS)
├── summarizer.py # Summarization logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🛠️ Installation

1. **Clone the repository**
git clone https://github.com/yourusername/NewsTopicTracker.git
cd NewsTopicTracker
Create virtual environment


---

## ✨ Features

- 🔍 **Select news category** from a dropdown (e.g., Business, Sports, Entertainment, etc.)
- 🤖 **Choose summarization method**:
  - Hugging Face Transformers
  - Ollama (Llama3)
- 📑 **Automatic news content extraction**
- 📜 **Short summaries** for each news article
- 🌐 **Clickable links** to read the full article

---

## 📋 Requirements

- Python **3.9+**
- Hugging Face Transformers
- Requests
- BeautifulSoup4
- Streamlit
- (Optional) Ollama installed locally

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/NewsTopicTracker.git
   cd NewsTopicTracker


▶️ Usage
Run the app:

streamlit run app.py
Open the link in your browser (usually http://localhost:8501).

📜 Example Output
less
Copy
Edit
1. Engineered Syn57 Bacteria Redefine the Genetic Code
[Read full article](https://www.biotecnika.org/...)

Summary:
Scientists have engineered a new strain of E. coli, Syn57, with only 57 codons...
🔧 Tech Stack
Python 3.9+

Streamlit – Interactive UI

GNews API – News data source

Hugging Face Transformers – Summarization

Ollama – Local LLaMA3 inference
