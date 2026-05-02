from flask import Flask, render_template, jsonify, request
from src.helper import load_vector_store
from src.prompt import system_prompt
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Load everything once when the server starts
print("Loading vector store...")
docsearch = load_vector_store()
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("Loading LLM...")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4,
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

print("✅ App ready!\n")


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    user_message = request.form["msg"]
    print(f"User: {user_message}")
    response = rag_chain.invoke({"input": user_message})
    answer = response["answer"]
    print(f"Bot: {answer}")
    return str(answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)