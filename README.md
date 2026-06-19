# Persona-Adaptive Customer Support Agent

An AI customer support assistant that uses retrieval-augmented generation, escalation detection, and handoff summaries to answer support questions from a local knowledge base.

## What It Does

- Answers user questions from the documents in `docs/`
- Uses Chroma to retrieve relevant support content
- Detects when a message should be escalated to a human agent
- Generates a short handoff summary when escalation is needed
- Includes a Gradio UI for chat-based interaction

## Project Structure

- `app.py` - CLI entry point and core chat logic
- `ui/gradio_ui.py` - Gradio frontend
- `agents/` - escalation detection and handoff summary helpers
- `rag/create_vectorstore.py` - builds the Chroma vector store from the knowledge base
- `docs/` - support knowledge base text files
- `chroma_db/` - local persisted vector store generated at build time

## Requirements

- Python 3.10+
- A `GEMINI_API_KEY` environment variable

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Gemini API key:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

## Build The Vector Store

Run the vector store script from the `rag/` directory so its relative paths resolve correctly:

```powershell
Set-Location rag
python create_vectorstore.py
Set-Location ..
```

This reads the text files in `docs/`, chunks them, and saves the embeddings to `chroma_db/`.

## Run The App

### CLI

```bash
python app.py
```

### Gradio UI

```bash
python ui/gradio_ui.py
```

The Gradio app launches on `http://0.0.0.0:7860` by default.

## Knowledge Base Topics

- Account recovery
- API authentication
- Billing policy
- Error codes
- Password reset
- Refund policy
- Security policy
- Service outage
- Subscription plans
- User management

## Notes

- If `chroma_db/` does not exist yet, build the vector store first.
- The assistant answers only from the retrieved context when possible.
- If escalation is triggered, it returns a human support handoff summary instead of a normal answer.
