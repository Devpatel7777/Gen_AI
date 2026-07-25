"""
AI Learning Coach - RAG Chatbot
"""

from dotenv import load_dotenv
load_dotenv()

import os
import uuid
import tempfile

import streamlit as st

from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

from langchain_core.tools import create_retriever_tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver


# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Learning Coach",
    page_icon="📘",
    layout="wide"
)


# ---------------- Heading ---------------- #

st.title("📘 AI Learning Coach - RAG Chatbot")
st.write("Upload one or more PDF files and ask questions from them.")


# ---------------- Models ---------------- #

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# ---------------- Session State ---------------- #

if "agent" not in st.session_state:
    st.session_state.agent = None

if "ready" not in st.session_state:
    st.session_state.ready = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())


# ---------------- Sidebar ---------------- #

st.sidebar.header("Project Features")

st.sidebar.write("📄 Multiple PDF Upload")
st.sidebar.write("📖 PDF Reading")
st.sidebar.write("✂️ Text Chunking")
st.sidebar.write("🧠 Gemini Embeddings")
st.sidebar.write("🗂️ InMemory Vector Store")
st.sidebar.write("🔍 Semantic Search")
st.sidebar.write("🤖 Groq GPT-OSS-20B")
st.sidebar.write("💬 AI Chat")
st.sidebar.write("🧠 Conversation Memory")


# ---------------- Upload PDFs ---------------- #

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

build = st.button("Build Knowledge Base")


# ---------------- Build Knowledge Base ---------------- #

if build:

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")

    else:

        documents = []
        temp_files = []

        with st.spinner("Reading PDF Files..."):

            for pdf in uploaded_files:

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp:

                    tmp.write(pdf.read())
                    temp_files.append(tmp.name)

                loader = PyPDFLoader(tmp.name)
                documents.extend(loader.load())

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        with st.spinner("Creating Vector Store..."):

            vector_store = InMemoryVectorStore.from_documents(
                documents=chunks,
                embedding=embeddings
            )

        retriever = vector_store.as_retriever(
            search_kwargs={"k": 4}
        )

        retriever_tool = create_retriever_tool(
            retriever,
            "pdf_search",
            """
Search information from uploaded PDF documents.

Always answer only from the uploaded PDFs.

If the answer is unavailable, reply:

I could not find that information in the uploaded documents.
"""
        )

        st.session_state.agent = create_agent(
            model=llm,
            tools=[retriever_tool],
            system_prompt="""
You are an AI Learning Coach.

Always use the pdf_search tool before answering.

Answer only from the uploaded PDF documents.
""",
            checkpointer=MemorySaver()
        )

        st.session_state.ready = True
        st.session_state.messages = []

        for file in temp_files:
            try:
                os.remove(file)
            except:
                pass

        st.success("Knowledge Base Created Successfully!")


# ---------------- Chat ---------------- #

if st.session_state.ready:

    st.divider()

    st.subheader("Chat with your PDFs")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask your question...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = st.session_state.agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    },
                    {
                        "configurable": {
                            "thread_id": st.session_state.thread_id
                        }
                    }
                )

                answer = response["messages"][-1].content

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

else:

    st.info("Upload PDF files and click 'Build Knowledge Base' to start.")