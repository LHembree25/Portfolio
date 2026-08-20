# Import library/packages
import streamlit as st
from transformers import pipeline

# Load fine-tuned model
pipe = pipeline(
    "text-generation",
    model="lex-gap-model",
    tokenizer="lex-gap-model",
    max_new_tokens=400,
    device_map="auto"
)

st.title("Gap Detection Model Demo")

st.write("Enter instructions. The model will return gap analysis in technician cadence.")

user_input = st.text_area("Instructions")

if st.button("Run"):
    if user_input.strip():

        system_prompt = """
Extract gaps only. No reproduction. No summary. No restatement.

You MUST anchor every gap to the document text.
You MUST cite exact lines from the document.
You MUST NOT invent new conditions, facts, or scenarios.
Each gap MUST reference the numbered step(s) where the issue appears.

Example gap (for pattern only):
Gap category: Undefined term
Gap statement: “car butt bonnet” is unclear and not a standard automotive term.
Supporting line(s): (1) Locate spare tyres (usually in the car butt bonnet)
Why it is a gap: The location description is ambiguous and may mislead the user.

Fill out the following template for each gap:

Gap category:
Gap statement:
Supporting line(s):
Why it is a gap:

Rules:
- Treat document as artifact under review.
- Only gap extraction.
- No hallucinated content.
"""

        full_prompt = (
    "DOCUMENT:\n"
    + user_input
    + "\n\nExtract ONE gap only.\n"
    + "Anchor the gap to the document text.\n"
    + "Cite exact line(s).\n"
    + "Do NOT invent anything not in the document.\n\n"
    + "Fill this template. The first field is already started — continue it:\n\n"
    + "Gap category: Undefined term\n"
    + "Gap statement:\n"
    + "Supporting line(s):\n"
    + "Why it is a gap:\n\n"
    + "=== END ==="
)

        result = pipe(full_prompt, max_new_tokens=400)[0]["generated_text"]
        st.write(result)

    else:
        st.write("No input provided.")