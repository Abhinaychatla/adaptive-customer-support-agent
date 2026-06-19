from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY=os.environ['GEMINI_API_KEY']

llm=init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)
def persona_detector(user_query):
    prompt=f"""
    You are customer persona classifier:
    classify the user into one category
    1.Technical Expert
    2.Frustrated user
    3.Business Executive
    Return only persona name
    "user message":
    {user_query}"""
    result=llm.invoke(prompt)
    return result.content
response=persona_detector("API authentication is failing with error 401")
print(response)


