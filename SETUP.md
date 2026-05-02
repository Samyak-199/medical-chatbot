# Medical Chatbot - Setup Notes

## Python Version
Python 3.11.9 (via pyenv)

## Virtual Environment
- Location: `./venv`
- Activate: `source venv/bin/activate`

## Installed Packages
Run `pip list` inside the venv to see all installed packages.

## To Resume Work
```bash
cd "/Users/samyakjain/My projects/Medical chatbot"
source venv/bin/activate
```

"""
langchain
langchain-groq
langchain-huggingface
langchain-community
sentence-transformers
pinecone
flask
pypdf
python-dotenv
"""

## Every time you want to run the project, just follow these steps:
## Step 1 — Open terminal in VSCode and navigate to project
bashcd "/Users/samyakjain/My projects/Medical chatbot"
## Step 2 — Activate the virtual environment
bashsource venv/bin/activate
## You should see (venv) appear in your terminal prompt.
## Step 3 — Run the app
bashpython app.py
## Step 4 — Open in browser
http://localhost:8080
