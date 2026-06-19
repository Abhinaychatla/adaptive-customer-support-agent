from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

from agents.escalation_checker import need_escalation
from agents.handoff_summary import generate_handoff_summary

load_dotenv()

llm = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=os.environ["GEMINI_API_KEY"]
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vector_store = Chroma(
    collection_name="customer_support",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

def retrieve_query(query, k=2):
    retrieved_docs = vector_store.similarity_search(query, k=k)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    return context, retrieved_docs

def docu_chat(user_query):

    escalation = need_escalation(user_query)

    print("Escalation:", escalation)

    if escalation:
        summary = generate_handoff_summary(user_query)

        return f"""
Escalated to Human Support

Handoff Summary:
{summary}
"""

    context, source_docs = retrieve_query(user_query)

    print("Retrieved Docs:", len(source_docs))
    print("Context:")
    print(context)

    system_message = f"""
You are a helpful customer support chatbot.

Answer ONLY from the provided context.

If the answer is not in the context, say:
"I couldn't find that information in the knowledge base."

Context:
{context}
"""

    response = llm.invoke([
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_query}
    ])

    return response.content

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    print(docu_chat(user_query))