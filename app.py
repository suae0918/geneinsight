import streamlit as st
from utils.pdf_parser import extract_text
from utils.summarize import summarize_text
from utils.keyword_extractor import extract_keywords, make_wordcloud
from utils.chatbot import ask_ai

st.set_page_config(page_title="GeneInsight", layout="wide")
st.title("🧬 GeneInsight: AI-Powered Research Dashboard")

# 1️⃣ PDF 업로드
uploaded_file = st.file_uploader("📂 Upload your PDF file", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)
    st.success("✅ PDF successfully extracted!")

    # 2️⃣ 요약 생성
    if st.button("🧠 Generate Summary"):
        summary = summarize_text(text)
        st.subheader("📘 Auto-Generated Summary")
        st.write(summary)

    # 3️⃣ 키워드 클라우드 생성
    if st.button("🧬 Generate Keyword Cloud"):
        keywords = extract_keywords(text)
        st.image(make_wordcloud(keywords), caption="Keyword Cloud")

    # 4️⃣ AI 질문 답변
    st.subheader("💬 Ask about this paper")
    user_q = st.text_input("Your question:")
    if user_q:
        answer = ask_ai(user_q, text)
        st.write(answer)
