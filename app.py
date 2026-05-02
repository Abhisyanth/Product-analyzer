import os

import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

groq_api_key = os.getenv("GROQ_API_KEY")


def clear_review_box() -> None:
    st.session_state["review_box"] = ""


st.set_page_config(page_title="E-Commerce Review Analyzer", layout="wide")
st.title("E-Commerce Review Analyzer")
st.write("Paste a product review and get a summary of the review")

st.write("## Paste a product review")
review = st.text_area("Review", height=200, key="review_box")

col_analyze, col_clear, _ = st.columns([1, 1, 4])
analyze = col_analyze.button("Analyze", type="primary")
col_clear.button("Clear", on_click=clear_review_box)

if analyze:
    if not groq_api_key:
        st.error("Missing GROQ_API_KEY. Add it to your .env file.")
    elif not review.strip():
        st.warning("Paste at least one review before analyzing.")
    else:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            groq_api_key=groq_api_key,
        )
        system = SystemMessage(
            content=(
                "You analyze e-commerce product reviews (Amazon, Flipkart, etc.). "
                "Respond in Markdown with these section headings exactly:\n"
                "## Positive themes\n"
                "## Negative themes\n"
                "## Overall sentiment\n"
                "## Key insights\n"
                "Base everything on the reviews the user pasted. If a topic is not in the reviews, say so briefly—do not invent."
            )
        )
        human = HumanMessage(content=review)
        response = llm.invoke([system, human])
        st.markdown(response.content)
    



