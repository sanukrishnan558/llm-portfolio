import streamlit as st
from transformers import pipeline
from utils.pdf_utils import extract_text_from_pdf

# Initialize summarizer
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit UI
st.set_page_config(page_title="Document Summarizer", layout="centered")
st.title("📄 Document Summarization Tool")
st.markdown("Upload a PDF document to generate its summary using Hugging Face Transformers.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.info("Extracting text from PDF...")
    full_text = extract_text_from_pdf(uploaded_file)

    if full_text.strip() == "":
        st.warning("No text could be extracted from the PDF.")
    else:
        st.success("Text extracted! Generating summary...")

        # BART has a max token limit, summarize in chunks if needed
        max_chunk_len = 1000
        chunks = [full_text[i:i+max_chunk_len] for i in range(0, len(full_text), max_chunk_len)]
        summaries = []

        for i, chunk in enumerate(chunks):
            with st.spinner(f"Summarizing chunk {i+1}/{len(chunks)}..."):
                summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
                summaries.append(summary)

        final_summary = " ".join(summaries)
        st.subheader("📌 Summary:")
        st.write(final_summary)

