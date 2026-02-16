# KodaStack MVP

Simple Streamlit prototype for "KodaStack.ai" — a minimal UI to transmute legacy COBOL into a modern Java service using a local Ollama model.

Prerequisites:
- Python 3.10+
- Install dependencies: `pip install -r requirements.txt`
- Run Ollama (local engine) and ensure the model `codellama:7b` is available, or adjust the model name in `app.py`.

Run:
1. pip install -r requirements.txt
2. streamlit run app.py

Notes:
- If the `ollama` package or server is unavailable, the app will show an error in the sidebar and fall back to a helpful message.
