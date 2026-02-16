import streamlit as st
import importlib
import json

st.set_page_config(page_title="KodaStack.ai | MVP", layout="wide")

# Custom CSS to make it look "Enterprise"
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; padding: 1rem; }
    .stButton>button { background-color: #c05621; color: white; border-radius: 5px; width: 100%; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(" KodaStack.ai")
st.subheader("Autonomous Legacy-to-Cloud Transmutation")

# Try to import the Ollama client; show helpful message if it's not available
ollama = None
try:
    ollama = importlib.import_module("ollama")
except Exception:
    st.sidebar.error("Warning: Python package 'ollama' not found. Install it or run Ollama locally to enable model calls.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📜 Legacy COBOL Source")
    legacy_code = st.text_area(
        "Paste COBOL here:",
        height=400,
        value="""IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
    DISPLAY 'Hello, World!'.
    STOP RUN.""",
    )

with col2:
    st.markdown("### ⚡ Modern Java Service")
    if st.button("Transmute to Java"):
        if not legacy_code.strip():
            st.warning("Please paste COBOL source to transmute.")
        else:
            with st.spinner("Analyzing business logic..."):
                # Professional Prompt Engineering
                prompt = f"""
Act as the KodaStack AI Architect.
1. Analyze the following COBOL code.
2. Extract the core business logic.
3. Rewrite it as a modern, high-performance Java Spring Boot class.
4. Include comments explaining the logic.

COBOL CODE:
{legacy_code}

JAVA OUTPUT:
"""
                if ollama is None:
                    st.error("Ollama client unavailable. Install the 'ollama' Python package and ensure the Ollama server is running.")
                else:
                    try:
                        # Attempt a best-effort call and render whatever the client returns.
                        # Different Ollama client versions return different shapes; handle common ones.
                        response = ollama.generate(model="codellama:7b", prompt=prompt)
                        output = None
                        if isinstance(response, dict):
                            # common keys checked in order
                            output = response.get("response") or response.get("text") or response.get("output") or response.get("content")
                            if output is None:
                                # fallback: pretty-print the dict
                                output = json.dumps(response, indent=2)
                        else:
                            output = str(response)

                        # Normalize common escaped sequences so newlines show correctly in the UI
                        if isinstance(output, str):
                            # Replace HTML breaks and escaped newlines with real newlines
                            output = output.replace("\\r\\n", "\n").replace("\\n", "\n").replace("<br/>", "\n").replace("<br>", "\n").replace("\\t", "\t")
                            # If the model returned a JSON-stringified object, try to unescape unicode escapes
                            try:
                                output = output.encode("utf-8").decode("unicode_escape")
                            except Exception:
                                # ignore decoding errors and keep current output
                                pass

                        # Display formatted code and provide a raw, scrollable area for copying
                        st.code(output, language="java")
                        st.text_area("Raw Java output (read-only)", value=output, height=300, disabled=True)
                        st.success("Transmutation Complete.")
                    except Exception as e:
                        st.error(f"Error calling Ollama: {e}")

st.sidebar.title("KodaStack Controls")
st.sidebar.write("Model: codellama:7b")
st.sidebar.write("Environment: Local Engine")