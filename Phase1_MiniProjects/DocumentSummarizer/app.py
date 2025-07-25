import streamlit as st
from transformers import pipeline
import PyPDF2

# Summarization pipeline using Hugging Face
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# PDF Text Extractor
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text

# Split text into chunks
def split_text(text, max_length=1024):
    words = text.split()
    chunks = []
    while words:
        chunk = words[:max_length]
        chunks.append(" ".join(chunk))
        words = words[max_length:]
    return chunks

# Summarize text in chunks and convert to points
def summarize_text(text):
    chunks = split_text(text)
    summarized_points = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        # Split into bullet points based on sentence end
        points = summary.split(". ")
        for point in points:
            point = point.strip().strip(".")
            if point:
                summarized_points.append(f"• {point}.")
    
    return summarized_points

# Streamlit UI
st.title("📄 Document Summarizer - Point by Point")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and summarizing..."):
        text = extract_text_from_pdf(uploaded_file)
        bullet_points = summarize_text(text)

    st.subheader("Summary:")
    for point in bullet_points:
        st.write(point)
