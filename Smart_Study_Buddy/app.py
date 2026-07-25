from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# ---------- Setup ----------
load_dotenv()  # .env mathi GOOGLE_API_KEY load thay

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

# ---------- Prompt Template ----------
STUDY_PROMPT = ChatPromptTemplate.from_template("""
You are an expert teacher.

Topic: {topic}
Difficulty Level: {difficulty}

Generate the following study material:

## Explanation
Explain the topic according to the selected difficulty.

## Simple Example
Give one simple example.

## Real-Life Example
Give one real-life example.

## 5 MCQs
Generate exactly 5 MCQs with:
- Question
- A, B, C, D options
- Correct Answer

## 5 Interview Questions
Generate 5 interview questions.

## Summary
Summarize the topic in bullet points.

Return everything in proper Markdown.
""")

chain = STUDY_PROMPT | llm

# ---------- Page Config ----------
st.set_page_config(page_title="Smart Study Buddy", page_icon="📚", layout="wide")
st.title("📚 Smart Study Buddy")
st.caption("Generate complete study material with Google Gemini")

# ---------- Layout ----------
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Topic", placeholder="Example: Python Functions")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    generate = st.button("🚀 Generate Study Material", use_container_width=True)

with col2:
    st.info(
        """
### Study Kit
- Explanation
- Simple Example
- Real-life Example
- 5 MCQs
- 5 Interview Questions
- Summary
"""
    )

# ---------- Generate ----------
if generate:
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        with st.spinner("Generating Study Material..."):
            response = chain.invoke({"topic": topic, "difficulty": difficulty})

        st.success("✅ Study Material Generated!")
        st.markdown("---")
        st.markdown(response.content)