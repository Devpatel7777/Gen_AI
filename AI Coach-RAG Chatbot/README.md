# 📘 AI Learning Coach – RAG Chatbot

## 📸 Application Preview

<p align="center">
  <img width="1911" height="922" alt="Screenshot 2026-07-25 180706" src="https://github.com/user-attachments/assets/c7b862e2-f7e3-4d81-8b19-164e3b68bf2e" />
  <img width="1482" height="717" alt="Screenshot 2026-07-25 180742" src="https://github.com/user-attachments/assets/57145077-0f47-4717-95c0-48b87d0013d5" />

</p>

---

# 🚀 Project Overview

**AI Learning Coach – RAG Chatbot** is an intelligent document-based conversational AI application that allows users to upload one or more PDF documents and ask questions in natural language.

The application leverages **Retrieval-Augmented Generation (RAG)** to retrieve the most relevant information from uploaded documents before generating responses using a Large Language Model (LLM). This approach minimizes hallucinations and ensures that answers remain grounded in the document content.

Built with **LangChain, LangGraph, Google Gemini Embeddings, InMemoryVectorStore, Groq GPT-OSS-20B, and Streamlit**, the chatbot serves as an AI-powered study companion capable of understanding books, research papers, resumes, manuals, notes, reports, and other PDF documents.

---

# 🎯 Business Problem

Students, researchers, and professionals often spend a significant amount of time searching through lengthy PDF documents to locate specific information.

Common challenges include:

- Reading hundreds of pages manually
- Searching information across multiple PDFs
- Slow document retrieval
- Difficulty finding relevant content
- Time-consuming research
- Information overload
- Reduced productivity

This project solves these challenges by enabling users to ask questions in natural language and instantly receive accurate answers extracted from uploaded PDF documents.

---

# 🎯 Project Objectives

- Build an AI-powered PDF Question Answering System
- Implement Retrieval-Augmented Generation (RAG)
- Enable Multiple PDF Understanding
- Generate Context-Aware Responses
- Reduce LLM Hallucinations
- Improve Information Retrieval
- Build an Interactive AI Chatbot
- Demonstrate Practical Generative AI Development

---

# ✨ Key Features

- 📄 Multiple PDF Upload
- 📚 Automatic PDF Reading
- ✂️ Intelligent Text Chunking
- 🧠 Google Gemini Embeddings
- 📦 InMemory Vector Store
- 🔍 Semantic Search
- 🤖 LangGraph AI Agent
- 💬 Conversational Chat Interface
- 🧠 Conversation Memory
- ⚡ Fast Retrieval
- 🎨 Responsive Streamlit UI

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| LLM | Groq GPT-OSS-20B |
| AI Framework | LangChain |
| Agent Framework | LangGraph |
| Embedding Model | Google Gemini Embeddings |
| Vector Store | InMemoryVectorStore |
| Document Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| Environment Variables | python-dotenv |

---

# ⚙️ Project Workflow

### Step 1 – Upload PDF Documents

Users upload one or more PDF documents through the Streamlit interface.

↓

### Step 2 – PDF Loading

The uploaded PDFs are processed using **PyPDFLoader**.

↓

### Step 3 – Text Chunking

Documents are divided into smaller overlapping chunks using **RecursiveCharacterTextSplitter**.

↓

### Step 4 – Embedding Generation

Each chunk is converted into vector embeddings using **Google Gemini Embeddings**.

↓

### Step 5 – Vector Storage

The embeddings are stored in **InMemoryVectorStore**.

↓

### Step 6 – Retriever Creation

A semantic retriever is created for similarity search.

↓

### Step 7 – LangGraph Agent

A LangGraph AI Agent is initialized with document retrieval capability.

↓

### Step 8 – User Question

The user asks questions related to uploaded documents.

↓

### Step 9 – Context Retrieval

The retriever fetches the most relevant document chunks.

↓

### Step 10 – AI Response

Groq GPT-OSS-20B generates an accurate answer using the retrieved context.

---

# 🧠 RAG Architecture

```

User

│

▼

Upload PDF Files

│

▼

PyPDFLoader

│

▼

Text Chunking

│

▼

Google Gemini Embeddings

│

▼

InMemoryVectorStore

│

▼

Retriever Tool

│

▼

LangGraph Agent

│

▼

Groq GPT-OSS-20B

│

▼

Final Response

```

---

# 💡 Prompt Engineering

The AI agent follows a carefully designed system prompt that instructs it to:

- Always retrieve information before answering
- Answer only using uploaded PDF documents
- Avoid generating unsupported information
- Clearly state when the requested information is unavailable
- Maintain conversational consistency

This significantly improves answer quality and minimizes hallucinations.

---

# 📂 Project Structure

```text
AI_Learning_Coach/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── Images/
│   ├── home.png
│   ├── upload.png
│   └── chat.png
│
└── PDFs/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI_Learning_Coach.git
```

---

## 2️⃣ Move into Project

```bash
cd AI_Learning_Coach
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create .env File

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## 5️⃣ Run Application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- Summarize this document.
- What are the main skills mentioned?
- Explain Chapter 3.
- What are the key findings?
- List all important dates.
- What is the conclusion?
- Explain this topic in simple language.

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- Google Gemini Embeddings
- Semantic Search
- AI Agents
- Prompt Engineering
- LLM Applications
- Streamlit Development
- Vector Search
- Conversational AI
- Python Development

---

# 🌍 Business Applications

- AI Study Assistant
- Resume Analyzer
- Research Paper Assistant
- Enterprise Knowledge Base
- Legal Document Search
- Technical Documentation Assistant
- Company Policy Chatbot
- Healthcare Knowledge Assistant
- Educational Platforms
- Internal Knowledge Management

---

# 🚀 Future Improvements

- DOCX Support
- PPT Support
- TXT Support
- Source Citations
- Conversation Export
- Voice Chat
- Multi-language Support
- User Authentication
- Cloud Deployment
- Persistent Conversation Memory

---

# 📸 Screenshots

## 🏠 Home Page

```
Images/home.png
```

## 📄 PDF Upload

```
Images/upload.png
```

## 💬 Chat Interface

```
Images/chat.png
```

---

# 📜 License

This project is developed for educational, learning, and portfolio purposes.

---

# 👨‍💻 Author

**Dev Patel**
