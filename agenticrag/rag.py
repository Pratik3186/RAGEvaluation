# agenticrag/rag.py

from langchain_core.messages import SystemMessage, HumanMessage
from retriever import get_retriever
from llm import get_llm
import streamlit as st

# ✅ cache heavy components
@st.cache_resource
def load_retriever():
    return get_retriever()

@st.cache_resource
def load_llm():
    return get_llm()

retriever = load_retriever()
llm = load_llm()


def rag_bot(question: str) -> dict:
    docs = retriever.invoke(question)
    docs = docs[:4]

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer the question.
If the answer is not in the context, say "I don't know."

Answer in maximum 3 sentences.

Context:
{context}
"""

    response = llm.invoke([
        SystemMessage(content=prompt),
        HumanMessage(content=question),
    ])

    return {
        "answer": response.content,
        "documents": docs
    }