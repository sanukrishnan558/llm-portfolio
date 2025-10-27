import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain

# Paths
DB_PATH = "chroma_db/"

st.set_page_config(page_title="📘 Conversational RAG Chatbot", page_icon="💬")
st.title("📘 Conversational RAG Chatbot with Ollama")

# 1️⃣ Initialize embeddings and vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})

# 2️⃣ Initialize Ollama LLM
llm = OllamaLLM(model="llama2", temperature=0)

# 3️⃣ Initialize conversational retrieval chain
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)

# 4️⃣ Maintain chat history in Streamlit session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 5️⃣ User input
query = st.text_input("Ask a question about your documents:")

if query:
    # Run the chain with history
    result = qa_chain({"question": query, "chat_history": st.session_state.chat_history})
    
    # Append new Q&A to history
    st.session_state.chat_history.append((query, result["answer"]))
    
    # Display full conversation
    for i, (q, a) in enumerate(st.session_state.chat_history):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
