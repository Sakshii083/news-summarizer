import streamlit as st
from summarizer import summarize, extract_keywords
from ai_summarizer import ai_summarize

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 AI News Summarizer")
st.caption("Summarize articles instantly with keyword insights 🚀")

mode = st.radio("Choose Mode", ["Basic NLP", "AI Model"])

col1, col2 = st.columns(2)

with col1:
    text = st.text_area("📄 Paste Article", height=300)
    num_sentences = st.slider("Summary Length", 1, 5, 3)
    analyze = st.button("✨ Analyze")

with col2:
    if analyze and text.strip():
        if mode == "Basic NLP":
            summary = summarize(text, num_sentences)
        else:
            summary = ai_summarize(text)

        keywords = extract_keywords(text)

        st.subheader("✂️ Summary")
        st.success(summary)

        st.subheader("🔑 Keywords")
        st.info(", ".join(keywords))

        words = len(text.split())
        summary_words = len(summary.split())

        st.metric("Original Words", words)
        st.metric("Summary Words", summary_words)
