from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.services.vector_store import get_embeddings, get_vectorstore_as_retriever
from app.config import (
    OPENAI_API_KEY, 
    OPENAI_MODEL_NAME,
    EMBEDDING_MODEL_NAME,
    PINECONE_INDEX_NAME,
)


def initialize_llm(**kwargs):
    openai_model_name = kwargs.get("openai_model_name", "gpt-4o")
    temperature = kwargs.get("temperature", 0.0)
    return ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name=openai_model_name,
        temperature=temperature
    )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def setup_rag_chain(retriever, **kwargs):
    prompt = hub.pull("rlm/rag-prompt")
    
    llm = initialize_llm(**kwargs)

    # Built-in chain
    # question_answer_chain = create_stuff_documents_chain(llm, prompt)
    # rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # LCEL
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain


def get_rag_chain():
    # Initialize embeddings and vector store
    embeddings = get_embeddings(EMBEDDING_MODEL_NAME)
    retriever = get_vectorstore_as_retriever(embeddings, PINECONE_INDEX_NAME)
    # Set up the RAG chain
    rag_chain = setup_rag_chain(
        retriever, 
        openai_model_name=OPENAI_MODEL_NAME, 
        temperature=0.0
    )
    return rag_chain
