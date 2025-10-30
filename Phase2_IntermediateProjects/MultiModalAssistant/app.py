import streamlit as st
from PIL import Image
from image_utils import caption_image, ocr_image
from retriever import Retriever
from llm_client import LLMClient

st.set_page_config(page_title="Multimodal Assistant", layout="wide")

# Custom CSS for better section headers
st.markdown("""
<style>
    .section-title {
        font-size: 1.5rem !important;
        font-weight: bold;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Centered main title
st.markdown("<h1 style='text-align: center;'>Multimodal Assistant — Text + Image (Ollama + LLaMA 3)</h1>", unsafe_allow_html=True)

llm = LLMClient(model="llama3")
retriever = Retriever(index_path="faiss_index.bin")

st.markdown("<div class='section-title'>Upload image</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

st.markdown("<div class='section-title'>Enter question</div>", unsafe_allow_html=True)
question = st.text_area("Ask something about the image or the content:", height=120)

if st.button("Submit"):
    if not question:
        st.warning("Please enter a question.")
    else:
        caption = ""
        ocr_text = ""

        # Process image if uploaded
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Uploaded image", use_container_width=True)

            with st.spinner("Generating caption & OCR..."):
                caption = caption_image(image)
                ocr_text = ocr_image(image)

        # Build multimodal context
        context_pieces = []
        if caption:
            context_pieces.append(f"Image caption: {caption}")
        if ocr_text:
            context_pieces.append(f"OCR text: {ocr_text}")

        # Retrieval
        retrieval_query = question
        if caption:
            retrieval_query += "\n" + caption

        with st.spinner("Retrieving related documents..."):
            docs = retriever.retrieve(retrieval_query, top_k=4)

        context_pieces.append("\n--- Retrieved documents ---")
        for i, d in enumerate(docs):
            context_pieces.append(f"Doc {i+1}: {d['text'][:500]}")

        # Final prompt
        context = "\n\n".join(context_pieces)
        prompt = (
            "You are a helpful assistant. Use the context below (image caption, OCR, and retrieved documents) "
            "to answer the user's question.\n"
            f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )

        # LLM answer
        with st.spinner("Generating answer from LLM..."):
            answer = llm.generate(prompt)

        st.subheader("Answer")
        st.write(answer)
