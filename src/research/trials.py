import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from helper import load_pdf_file, text_split, get_embedding_model

# Test 1 - Load PDF
data_path = "/Users/samyakjain/My projects/Medical chatbot/data/medical_book.pdf"

documents = load_pdf_file(data_path)
print(f"Total pages loaded: {len(documents)}")
print(f"\nSample from page 1:\n{documents[0].page_content[:300]}")

# Test 2 - Split into chunks
chunks = text_split(documents)
print(f"\nTotal chunks created: {len(chunks)}")
print(f"\nSample chunk:\n{chunks[10].page_content}")

# Test 3 - Embedding model
embedding_model = get_embedding_model()
test_vector = embedding_model.embed_query("What is diabetes?")
print(f"\nEmbedding vector length: {len(test_vector)}")
print(f"First 5 values: {test_vector[:5]}")