from src.helper import load_pdf_file, text_split, get_embedding_model
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# Step 1 - Load and chunk the PDF
print("Loading PDF...")
documents = load_pdf_file("data/medical_book.pdf")
chunks = text_split(documents)
print(f"Total chunks to index: {len(chunks)}")

# Step 2 - Load embedding model
print("\nLoading embedding model...")
embeddings = get_embedding_model()

# Step 3 - Connect to Pinecone
print("\nConnecting to Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

# Step 4 - Push all chunks + their vectors into Pinecone
print("\nIndexing chunks into Pinecone... (this will take a few minutes)")
docsearch = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    index_name=index_name
)

print("\n✅ Done! All chunks indexed into Pinecone successfully.")