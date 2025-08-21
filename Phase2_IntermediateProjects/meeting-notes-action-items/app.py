import streamlit as st
import subprocess
import tempfile
from faster_whisper import WhisperModel
import ollama

# Load Whisper model (choose tiny, base, small, medium, large-v3)
WHISPER_MODEL = "small"

st.title("🎙️ Meeting Notes & Action Item Extractor (Local)")

uploaded_file = st.file_uploader("Upload meeting audio", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        audio_path = tmp_file.name

    st.info("⏳ Transcribing audio...")

    # Load whisper model
    model = WhisperModel(WHISPER_MODEL, device="cpu")
    segments, info = model.transcribe(audio_path)

    transcript = " ".join([segment.text for segment in segments])
    st.subheader("📜 Transcript")
    st.write(transcript)

    st.info("⏳ Generating notes & action items with local LLM (Ollama)...")

    prompt = f"""
    You are an assistant that extracts meeting notes and action items.
    
    Transcript:
    {transcript}

    Please provide:
    1. A structured summary of key discussion points.
    2. A bullet list of clear action items with owners if mentioned.
    """

    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])

    st.subheader("📝 Meeting Notes & Action Items")
    st.write(response["message"]["content"])
