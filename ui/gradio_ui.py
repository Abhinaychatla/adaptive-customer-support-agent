import gradio as gr
from app import docu_chat


def chat(user_query):
    try:
        response = docu_chat(user_query)
        return response

    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Ask a customer support question..."
    ),
    outputs=gr.Textbox(
        lines=15,
        label="Response"
    ),
    title="Persona-Adaptive Customer Support Agent",
    description="""
RAG + Gemini + Human Escalation

Example Queries:

Knowledge Base Questions:
• What is your refund policy?
• How do I reset my password?
• What subscription plans are available?
• How can I recover my account?
• What does error code AUTH_401 mean?

Escalation Questions:
• I want a human agent.
• Connect me to support.
• I want to speak with a manager.
• Escalate this issue.
"""
)



if __name__ == "__main__":
    demo.launch()