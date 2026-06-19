from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY=os.environ['GEMINI_API_KEY']
llm=init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)

def need_escalation(user_query):
    prompt=f"""
You are an escalation detection system for a customer support agent.

Determine whether the following customer query should be escalated to a human support representative.

Escalate if:
- The customer is angry, frustrated, or abusive.
- The customer requests a manager or human agent.
- The issue involves legal action.
- The issue involves account closure or serious billing disputes.
- The issue cannot be resolved through standard support policies.

Respond with only:
YES
or
NO

customer query:
{user_query}
    """
    response=llm.invoke(prompt)
    return response.content.strip().upper() == "YES"
