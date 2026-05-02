from src.helper import load_vector_store
from src.prompt import system_prompt
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 - Load vector store as retriever
print("Loading vector store...")
docsearch = load_vector_store()
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # fetch top 3 most relevant chunks
)

# Step 2 - Load Groq LLM (free Llama3)
print("Loading LLM...")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4,
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

# Step 3 - Build the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Step 4 - Build the RAG chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Step 5 - Ask a medical question!
print("\nAsking a question...\n")
response = rag_chain.invoke({"input": "What are the symptoms of diabetes?"})

print(f"Answer:\n{response['answer']}")