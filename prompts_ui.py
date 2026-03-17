from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=1)

## creating the template for dynamic prompts


st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
        "Gemini",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical",
        "FlowCharts Oriented",
    ],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

template = load_prompt("template.json")

## filling the placeholders
user_prompt = template.invoke(
    {
        "paper_name": paper_input,
        "input_style": style_input,
        "input_length": length_input,
    }
)


if st.button("Summarize"):
    result = model.invoke(user_prompt)
    st.write(result.content)
