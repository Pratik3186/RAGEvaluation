# 🤖 RAG Evaluation System (Ollama + LangChain)

A complete **Retrieval-Augmented Generation (RAG)** system with **LLM-based evaluation metrics**, built using LangChain, Ollama, and Streamlit.

---

## 🚀 Features

* 🔍 **RAG Pipeline**

  * Web-based document ingestion
  * Chunking & embedding using HuggingFace
  * Vector search with retriever

* 🧠 **Local LLM (Ollama - Llama3)**

  * No API cost
  * Fully local inference

* 📊 **Evaluation System (LLM-as-a-Judge)**

  * ✅ Correctness
  * 🎯 Relevance
  * 🔒 Groundedness (hallucination detection)
  * 📄 Retrieval Relevance

* 🖥️ **Streamlit UI**

  * Ask questions interactively
  * View retrieved documents
  * Clean chatbot interface

---

## 🛠️ Tech Stack

* **LangChain**
* **Ollama (Llama3)**
* **HuggingFace Embeddings**
* **Streamlit**
* **LangSmith (Evaluation)**

---

## 🧠 Architecture

```
User Question
      ↓
Retriever (Vector DB)
      ↓
Relevant Documents
      ↓
LLM (Ollama - Llama3)
      ↓
Generated Answer
      ↓
Evaluation Metrics
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/RAGEvaluation.git
cd RAGEvaluation

pip install -r requirements.txt
```

---

## ▶️ Run the App

### Step 1: Start Ollama

```bash
ollama run llama3
```

### Step 2: Run Streamlit

```bash
cd agenticrag
streamlit run app.py
```

---

## 📊 Evaluation Metrics Explained

| Metric              | Description                         |
| ------------------- | ----------------------------------- |
| Correctness         | Checks factual accuracy             |
| Relevance           | Checks if answer addresses question |
| Groundedness        | Detects hallucination               |
| Retrieval Relevance | Checks document quality             |

---

## 🔥 Key Learnings

* Built a full **RAG system from scratch**
* Implemented **LLM-based evaluation (industry-level)**
* Handled **real-world issues (CUDA, dependencies, deployment)**
* Designed **modular AI architecture**

---

## 🚀 Future Improvements

* Chat memory (conversation history)
* PDF / file upload support
* Deployment with cloud LLMs
* Dashboard for evaluation metrics

---

## 👨‍💻 Author

**Pratik**

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!


