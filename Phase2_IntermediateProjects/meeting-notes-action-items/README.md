# 🎙️ Meeting Notes & Action Item Extractor (Local)

A simple Streamlit app that: 1. Transcribes meeting audio using [Faster
Whisper](https://github.com/guillaumekln/faster-whisper). 2. Extracts
structured notes & action items using [Ollama](https://ollama.ai/)
(local LLM).

## 🚀 Setup & Run

1.  Clone this repo:

    ``` bash
    git clone https://github.com/sanukrishnan558/llm-portfolio.git
    cd llm-portfolio/Phase2_IntermediateProjects/meeting-notes-action-items
    ```

2.  Create & activate virtual environment:

    ``` bash
    python -m venv .venv
    .venv\Scripts\activate    # Windows
    source .venv/bin/activate # Linux/Mac
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Make sure [Ollama](https://ollama.ai/) is installed and running with
    `llama3`:

    ``` bash
    ollama pull llama3
    ```

5.  Run the app:

    ``` bash
    streamlit run app.py
    ```

6.  Open in browser: <http://localhost:8501>

## 📝 Example Workflow

-   Upload an audio file (`.mp3`, `.wav`, `.m4a`).
-   The app transcribes the audio to text.
-   A local LLM (llama3 via Ollama) generates structured meeting notes
    and action items.
