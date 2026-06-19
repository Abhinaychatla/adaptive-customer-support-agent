from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY=os.environ['GEMINI_API_KEY']
llm=init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)
def generate_handoff_summary(user_query):
    prompt = f"""
Create a concise support handoff summary.

Customer Message:
{user_query}

Include:
1. Issue
2. Customer Sentiment
3. Reason for Escalation
4. Recommended Action

Keep it under 100 words.
"""
    response=llm.invoke(prompt)
    return response.content