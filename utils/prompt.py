# def build_prompt(context_chunks, query):
#     context = "\n\n".join(context_chunks)
#     return f"""Use the context below to answer the question.

# Context:
# {context}

# Question:
# {query}

# Answer:"""

def build_prompt(context_chunks, query):

    context = "\n\n".join(context_chunks)

    return f"""
You are a Product Management assistant.

Use ONLY the information provided in the context.

If the answer is not available in the context, say:

"I couldn't find the answer in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""