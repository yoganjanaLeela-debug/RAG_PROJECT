# 📄 Resume Analysis using Retrieval-Augmented Generation (RAG)

A Retrieval-Augmented Generation (RAG) application that enables intelligent question answering over multiple PDF resumes using **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and a **local Ollama Large Language Model (LLM)**.

The system retrieves the most relevant information from uploaded resumes before generating accurate, context-aware responses.

---

# 📖 Project Overview

Traditional Large Language Models cannot answer questions about private documents unless those documents are included in the prompt. This project solves that limitation using the Retrieval-Augmented Generation (RAG) architecture.

The application loads multiple resumes, converts them into vector embeddings, stores them in ChromaDB, retrieves the most relevant document chunks for a user's question, and uses a local LLM to generate accurate answers based solely on the retrieved context.

---

# ✨ Features

* 📄 Load multiple PDF resumes
* ✂️ Automatic document chunking
* 🧠 Semantic search using embeddings
* 📚 ChromaDB vector database
* 🤖 Local LLM inference with Ollama
* ⚡ Fast similarity search
* 🔍 Context-aware question answering
* 🔒 Completely offline after model setup
* 🚀 Easy to extend for any document collection

---

# 🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers
* Ollama
* Phi-3 LLM
* Recursive Character Text Splitter

---

# 📂 Project Structure

```text
RAG_PROJECT/
│
├── app.py
├── resume1.pdf
├── resume2.pdf
├── resume3.pdf
├── chroma_db/
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yoganjanaLeela-debug/RAG_PROJECT.git
```

## Navigate to the Project

```bash
cd RAG_PROJECT
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download Ollama from:

https://ollama.com

Pull the Phi-3 model:

```bash
ollama pull phi3
```

---

# ▶️ Run the Project

```bash
python app.py
```

Ask questions such as:

```text
Who has experience in Machine Learning?

Which candidate knows Python?

Who has worked with Deep Learning?

Summarize Resume 2.

Which candidate has the strongest AI background?
```

Type:

```text
exit
```

to close the application.

---

# 🔄 Workflow

```text
PDF Resumes
      │
      ▼
Load Documents
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Generate Response using Phi-3 (Ollama)
```

---

# 🧠 RAG Pipeline

1. Load PDF resumes.
2. Split documents into manageable chunks.
3. Generate vector embeddings using Sentence Transformers.
4. Store vectors in ChromaDB.
5. Accept a user query.
6. Retrieve the most relevant document chunks.
7. Send the retrieved context to the local LLM.
8. Generate an accurate answer grounded in the retrieved content.

---

# 🎯 Applications

* Resume Screening
* HR Candidate Search
* Recruitment Automation
* Enterprise Knowledge Base
* Document Question Answering
* Research Paper Search
* Legal Document Analysis
* Policy & Compliance Assistant

---

# 📚 Learning Outcomes

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embedding Models
* LangChain Framework
* Local LLM Deployment
* Prompt Engineering
* Document Intelligence

---

# 🚀 Future Enhancements

* Streamlit Web Interface
* Drag-and-drop PDF upload
* Multi-document comparison
* Chat history and memory
* Support for DOCX and TXT files
* Metadata filtering
* Hybrid search (keyword + semantic)
* Integration with cloud LLMs (Gemini, OpenAI, Claude)

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Submit a Pull Request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Yoganjana**

* GitHub: https://github.com/yoganjanaLeela-debug

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
