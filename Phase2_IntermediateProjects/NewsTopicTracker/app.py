# app.py
import streamlit as st
from news_scraper import fetch_trending_news
from article_parser import extract_article_content
from summarizer import summarize_text

st.set_page_config("📰 News Topic Tracker")

st.title("📰 News Topic Tracker")

news_items = fetch_trending_news()

for i, (title, link) in enumerate(news_items):
    with st.expander(f"{i+1}. {title}"):
        if st.button("Summarize", key=f"summarize_{i}"):
            with st.spinner("Fetching and summarizing..."):
                content = extract_article_content(link)
                summary = summarize_text(content)
                st.markdown(f"**Summary:**\n{summary}")
        st.markdown(f"[Read Full Article]({link})", unsafe_allow_html=True)
