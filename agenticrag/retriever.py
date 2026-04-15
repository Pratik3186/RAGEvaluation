# agenticrag/retriever.py

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_retriever():
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]

    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=0
    )

    doc_splits = text_splitter.split_documents(docs_list)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}   # ✅ avoid CUDA issues
    )

    vectorstore = InMemoryVectorStore.from_documents(
        documents=doc_splits,
        embedding=embedding_model,
    )

    return vectorstore.as_retriever(search_kwargs={"k": 4})