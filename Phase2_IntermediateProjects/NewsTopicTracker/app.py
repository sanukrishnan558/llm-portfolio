import streamlit as st
from news_scraper import get_top_news, CATEGORIES
from summarizer import summarize_text
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="📰 News Topic Tracker", layout="centered")
st.title("📰 News Topic Tracker")

st.markdown("Get top news from India by category and summarize them using Hugging Face or Ollama (Llama3).")

# Category dropdown
category = st.selectbox("Choose a news category:", list(CATEGORIES.keys()))

# Model selection
method = st.radio("Choose summarization method:", ["Hugging Face", "Ollama (Llama3)"])

if st.button("Fetch & Summarize News"):
    with st.spinner("Getting latest headlines..."):
        headlines = get_top_news(category)

        for idx, article in enumerate(headlines, start=1):
            st.subheader(f"{idx}. {article['title']}")
            st.markdown(f"[Read full article]({article['url']})")

            try:
                # 1️⃣ Use GNews content if available
                text = article.get("content", "")

                # 2️⃣ If content is missing, scrape the webpage
                if not text or len(text.split()) < 30:
                    article_html = requests.get(article["url"], timeout=5).text
                    soup = BeautifulSoup(article_html, "html.parser")
                    paras = soup.find_all("p")
                    text = " ".join([p.text for p in paras][:10])

                # 3️⃣ Summarize the extracted text
                summary = summarize_text(text, "ollama" if method == "Ollama (Llama3)" else "huggingface")

            except Exception as e:
                summary = f"❌ Could not summarize article: {e}"

            st.markdown("**Summary:**")
            st.info(summary)
