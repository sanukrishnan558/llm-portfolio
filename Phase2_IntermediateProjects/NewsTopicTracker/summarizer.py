from transformers import pipeline
import subprocess

# Hugging Face Summarizer
hf_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_with_huggingface(text):
    if not text or len(text.split()) < 15:
        return "⚠️ Not enough content to summarize."

    try:
        text = " ".join(text.split()[:500])  # Trim to avoid token overflow
        summary = hf_summarizer(text, max_length=60, min_length=20, do_sample=False)
        return summary[0]["summary_text"] if summary else "⚠️ No summary generated."
    except Exception as e:
        return f"❌ Hugging Face error: {e}"

def summarize_with_ollama(text):
    if not text or len(text.split()) < 15:
        return "⚠️ Not enough content to summarize."

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", f"Summarize this text in 2-3 sentences:\n\n{text}"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() if result.stdout else "⚠️ No response from Ollama."
    except Exception as e:
        return f"❌ Ollama error: {e}"

def summarize_text(text, method="huggingface"):
    return summarize_with_ollama(text) if method == "ollama" else summarize_with_huggingface(text)
