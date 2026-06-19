import streamlit as st

from utils.retrieval import (
    load_faiss_index,
    retrieve_chunks
)
from utils.prompt import build_prompt
from utils.completion import generate_completion


@st.cache_resource
def get_index():
    return load_faiss_index()


st.title("Product Management RAG Chatbot")

st.write(
    "Ask questions about Product Management, Product Ownership, Agile, Scrum, Roadmaps, Prioritization, Stakeholder Management, and related topics."
)

query = st.text_input("Ask your question")

if query:

    try:

        index, chunk_mapping = get_index()

        with st.spinner("Searching knowledge base..."):

            top_chunks = retrieve_chunks(
                query,
                index,
                chunk_mapping
            )

            prompt = build_prompt(
                top_chunks,
                query
            )

            response = generate_completion(
                prompt
            )

        st.subheader("Answer")
        st.write(response)

        with st.expander("Retrieved Chunks"):

            for i, chunk in enumerate(top_chunks, start=1):
                st.markdown(f"**Chunk {i}:**")
                st.write(chunk)

    except Exception as e:

        st.error(
            f"Something went wrong: {e}"
        )