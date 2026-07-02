from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)

def build_rag_chain(retriever):

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=1
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa_chain