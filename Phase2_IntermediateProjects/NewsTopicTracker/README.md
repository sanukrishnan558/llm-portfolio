# 📰 News Topic Tracker

A simple and interactive **Streamlit** application to fetch and summarize the latest news from India by category.  
You can choose between **Hugging Face** or **Ollama (Llama3)** for summarization.

---

## 📂 Project Structure

```
NewsTopicTracker/
│
├── app.py               # Main Streamlit app
├── news_scraper.py      # News fetching logic (GNews API / RSS)
├── summarizer.py        # Summarization logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

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
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the root directory with:
   ```env
   GNEWS_API_KEY=your_gnews_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## ⚙️ Configuration

You can adjust:
- **News sources & categories** → in `news_scraper.py`
- **Summarization model** → in `summarizer.py`
- **Default summarization method** → in `app.py`

---

## 📷 Screenshots

<img width="1919" height="894" alt="image" src="https://github.com/user-attachments/assets/55af4004-ab97-4bbe-b71c-f8108510b0f5" />


---

## 🛠 Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/)
- [GNews API](https://gnews.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---

## 📌 Future Improvements

- ✅ Support for more summarization models
- ✅ Option to download summaries as PDF/CSV
- ✅ Dark mode UI theme

---

## 🤝 Contributing

Pull requests are welcome! Please fork the repo and submit a PR for any improvements.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
