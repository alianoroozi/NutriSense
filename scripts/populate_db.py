from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from app.services.document_loader import load_pdf_files, get_text_chunks
from app.services.vector_store import get_embeddings
from app.config import (
    EMBEDDING_MODEL_NAME, 
    PINECONE_INDEX_NAME, 
    CHUNK_SIZE, 
    CHUNK_OVERLAP
)


if __name__ == "__main__":
    load_dotenv()

    chunk_size = CHUNK_SIZE
    chunk_overlap = CHUNK_OVERLAP
    embedding_model_name = EMBEDDING_MODEL_NAME
    index_name = PINECONE_INDEX_NAME
    data_dir = "docs/pdfs/"

    print("Loading PDF documents and splitting into text chunks ...")
    docs = load_pdf_files(data_dir)
    print("Total number of documents:", len(docs))

    text_chunks = get_text_chunks(docs, chunk_size, chunk_overlap)
    print("Total number of text chunks:", len(text_chunks))

    print("Initializing embeddings ...")
    embeddings = get_embeddings(embedding_model_name)

    print("Populating vector store with document embeddings ...")
    PineconeVectorStore.from_documents(
        documents=text_chunks,
        embedding=embeddings,
        index_name=index_name
    )
    print("Vector store population completed.")
