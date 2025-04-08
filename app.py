import streamlit as st
from utils.transcript_utils import get_transcript
from utils.summarizer import summarize_transcript
from utils.quiz_generator import generate_quiz
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="Lecture Summarizer", layout="centered")
st.title("📚 YouTube Lecture Summarizer Agent")
st.markdown("Turn any YouTube lecture into clean notes and quizzes using AI. Just paste the URL and hit enter!")

video_url = st.text_input("🎥 Paste a YouTube lecture URL:", placeholder="https://www.youtube.com/watch?v=ZXiruGOCn9s")

if video_url:
    if "transcript" not in st.session_state:
        st.markdown("#### Step 1: 📄 Get Transcript")
        with st.spinner("Getting transcript..."):
            st.session_state.transcript = get_transcript(video_url)

    with st.expander("📖 View Full Transcript"):
        st.write(st.session_state.transcript)

    if "summary" not in st.session_state:
        st.markdown("#### Step 2: ✍️ Summarization")
        with st.spinner("Summarizing..."):
            st.session_state.summary = summarize_transcript(st.session_state.transcript)

    st.subheader("📝 Lecture Notes")
    st.markdown(st.session_state.summary)

    st.markdown("---")

    if "quiz" not in st.session_state:
        st.markdown("#### Step 3: ❓ Quiz Generation")
        with st.spinner("Generating quiz..."):
            st.session_state.quiz = generate_quiz(st.session_state.transcript)

    st.subheader("🧠 Quiz Questions")
    st.markdown(st.session_state.quiz)

    st.markdown("---")

    if "pdf_bytes" not in st.session_state:
        with st.spinner("Generating PDF..."):
            st.session_state.pdf_bytes = generate_pdf(st.session_state.summary, st.session_state.quiz)

    st.download_button(
        label="📥 Download Notes + Quiz as PDF",
        data=st.session_state.pdf_bytes,
        file_name="youtube_lecture_summary.pdf",
        mime="application/pdf"
    )

    st.success("✅ All done! You can review, revise, or download your AI-powered study material.")
