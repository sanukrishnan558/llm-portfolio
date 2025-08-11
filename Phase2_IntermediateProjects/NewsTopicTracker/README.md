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
├── app.py # Streamlit app entry point
├── news_scraper.py # Fetches news from GNews API
├── summarizer.py # Summarization logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Installation

1. **Clone the repository**
git clone https://github.com/yourusername/NewsTopicTracker.git
cd NewsTopicTracker
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory:

env
Copy
Edit
GNEWS_API_KEY=your_gnews_api_key
Get your API key from: https://gnews.io

▶️ Usage
Run the app:

bash
Copy
Edit
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
