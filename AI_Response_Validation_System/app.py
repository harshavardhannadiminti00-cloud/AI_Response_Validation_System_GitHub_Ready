import re
import math
import streamlit as st
from difflib import SequenceMatcher

st.set_page_config(page_title="AI Response Validation System", page_icon="🤖", layout="wide")

def clean_text(text):
    return re.sub(r"\s+", " ", text.strip())

def split_sentences(text):
    text = clean_text(text)
    if not text:
        return []
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def factual_support(sentence, reference):
    s_tokens = tokenize(sentence)
    r_tokens = tokenize(reference)
    if not s_tokens:
        return 0.0
    return len(s_tokens & r_tokens) / len(s_tokens)

def validate_response(response, reference):
    response = clean_text(response)
    reference = clean_text(reference)

    if not response:
        return {"score": 0, "status": "No response", "flags": ["Enter an AI response."]}

    if not reference:
        return {
            "score": 50,
            "status": "Reference missing",
            "flags": ["Add reference/context text for stronger hallucination detection."]
        }

    sentences = split_sentences(response)
    ref_sentences = split_sentences(reference)
    details = []
    supported = 0

    for sentence in sentences:
        support = factual_support(sentence, reference)
        best_sim = max((similarity(sentence, r) for r in ref_sentences), default=0)
        confidence = min(100, round((0.65 * support + 0.35 * best_sim) * 100))

        if confidence >= 65:
            label = "Likely Supported"
            supported += 1
        elif confidence >= 35:
            label = "Partially Supported"
        else:
            label = "Potential Hallucination"

        details.append({
            "sentence": sentence,
            "confidence": confidence,
            "label": label
        })

    score = round((supported / max(1, len(sentences))) * 100)
    hallucinations = sum(1 for d in details if d["label"] == "Potential Hallucination")

    if hallucinations:
        status = "Review Required"
    elif score >= 70:
        status = "Likely Reliable"
    else:
        status = "Needs Review"

    return {"score": score, "status": status, "flags": [], "details": details}

st.title("🤖 AI Response Validation System")
st.caption("Hallucination Detection Assistance — project prototype")

col1, col2 = st.columns(2)
with col1:
    response = st.text_area(
        "AI Response",
        height=280,
        placeholder="Paste the AI-generated answer here..."
    )

with col2:
    reference = st.text_area(
        "Reference / Ground Truth",
        height=280,
        placeholder="Paste trusted information, source text, or expected answer here..."
    )

if st.button("Validate Response", type="primary", use_container_width=True):
    result = validate_response(response, reference)

    st.divider()
    a, b, c = st.columns(3)
    a.metric("Validation Score", f"{result['score']}%")
    b.metric("Status", result["status"])
    c.metric("Sentences Checked", len(result.get("details", [])))

    if result["flags"]:
        for flag in result["flags"]:
            st.warning(flag)

    if result.get("details"):
        st.subheader("Sentence-level Analysis")
        for item in result["details"]:
            if item["label"] == "Potential Hallucination":
                st.error(f"⚠️ {item['label']} — {item['confidence']}% confidence\n\n{item['sentence']}")
            elif item["label"] == "Partially Supported":
                st.warning(f"🟡 {item['label']} — {item['confidence']}% confidence\n\n{item['sentence']}")
            else:
                st.success(f"✅ {item['label']} — {item['confidence']}% confidence\n\n{item['sentence']}")

        st.info(
            "Note: This prototype uses text-overlap and similarity heuristics. "
            "It is an assistance tool, not a replacement for expert fact-checking."
        )
else:
    st.markdown(
        """
### How it works
1. Paste an AI-generated response.
2. Paste trusted reference/context information.
3. Click **Validate Response**.
4. The system compares each response sentence with the reference.
5. It highlights sentences that may need hallucination review.
        """
    )
