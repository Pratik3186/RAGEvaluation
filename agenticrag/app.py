# agenticrag/app.py

import streamlit as st
from rag import rag_bot

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🤖 RAG Chatbot (Ollama + LangChain)")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            result = rag_bot(question)

            st.subheader("📌 Answer")
            st.write(result["answer"])

            st.subheader("📄 Retrieved Documents")
            for i, doc in enumerate(result["documents"]):
                st.markdown(f"**Doc {i+1}:**")
                st.write(doc.page_content[:300] + "...")
    else:
        st.warning("Please enter a question")