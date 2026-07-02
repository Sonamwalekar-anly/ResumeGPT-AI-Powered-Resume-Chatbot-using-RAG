from langchain_community.vectorstores import Chroma
from config import CHROMA_PATH

def create_vector_store(chunks, embeddings):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    vectorstore.persist()

    return vectorstore