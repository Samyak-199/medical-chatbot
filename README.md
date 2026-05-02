# 🏥 Medical Chatbot — RAG-Powered AI Assistant

A fully functional medical chatbot built with **Retrieval-Augmented Generation (RAG)**. Ask it anything about symptoms, conditions, or treatments — it retrieves relevant information from the Gale Encyclopedia of Medicine and generates accurate, grounded answers using Llama 3.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![Flask](https://img.shields.io/badge/Flask-latest-lightgrey)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-purple)
![Groq](https://img.shields.io/badge/Groq-Llama%203-orange)

---

## 🧠 How It Works

```
User Question
     │
     ▼
[HuggingFace Embeddings]   ← converts question to a vector
     │
     ▼
[Pinecone Vector DB]       ← finds top 3 most relevant chunks
     │                        from 9000+ indexed medical passages
     ▼
[Groq / Llama 3]           ← reads retrieved chunks + question
     │                        and generates a grounded answer
     ▼
[Flask Web UI]             ← displays the answer in the browser
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.1 8B (via Groq API — free) |
| Embeddings | `all-MiniLM-L6-v2` (HuggingFace — local, free) |
| Vector Database | Pinecone (free tier) |
| Orchestration | LangChain |
| Web Framework | Flask |
| Data Source | Gale Encyclopedia of Medicine (PDF) |

---

## 📁 Project Structure

```
medical-chatbot/
│
├── data/                    ← Medical PDF source
├── src/
│   ├── __init__.py
│   ├── helper.py            ← PDF loading, chunking, embedding, vector store
│   └── prompt.py            ← System prompt template
├── templates/
│   └── chat.html            ← Chat UI
├── static/                  ← CSS assets
├── store_index.py           ← One-time indexing script
├── app.py                   ← Flask application
├── requirements.txt
├── setup.py
├── .env                     ← API keys (not committed)
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- A free [Groq API key](https://console.groq.com)
- A free [Pinecone API key](https://app.pinecone.io)

### Step 1 — Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/medical-chatbot.git
cd medical-chatbot
```

### Step 2 — Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
pip install -e .
```

### Step 4 — Set up environment variables
Create a `.env` file in the root directory:
```
PINECONE_API_KEY="your-pinecone-api-key"
GROQ_API_KEY="your-groq-api-key"
```

### Step 5 — Add your data
Place your medical PDF in the `data/` folder and name it `medical_book.pdf`.

### Step 6 — Index the data (one-time only)
```bash
python store_index.py
```
This embeds the entire PDF and uploads it to Pinecone. Takes ~5 minutes.

### Step 7 — Run the app
```bash
python app.py
```

Open your browser and go to:
```
http://localhost:8080
```

---

## 💬 Example Questions

- *What are the symptoms of diabetes?*
- *How is hypertension treated?*
- *What causes anemia?*
- *What is the difference between Type 1 and Type 2 diabetes?*

---

## ⚠️ Disclaimer

This chatbot is for **educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## 🙏 Credits

- Original project concept by [DSwithBappy](https://www.youtube.com/@DSwithBappy)
- Modified to use open-source/free stack (Groq + HuggingFace) instead of OpenAI
