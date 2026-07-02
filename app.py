from src.pdf_loader import load_pdf
from src.chunking import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.rag_chain import build_rag_chain

print("Loading PDF...")

docs = load_pdf("data/data analytics res (1).pdf")

chunks = split_documents(docs)
""
embeddings = get_embedding_model()

vectorstore = create_vector_store(
    chunks,
    embeddings
)

retriever = get_retriever(vectorstore)

qa_chain = build_rag_chain(retriever)

print("RAG Chatbot Ready!")

while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        break

    response = qa_chain.invoke(query)

    print("\nAnswer:")
    print(response["result"])