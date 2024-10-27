from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


def get_embeddings(embedding_model_name):
    return OpenAIEmbeddings(model=embedding_model_name)


def get_vectorstore_as_retriever(embeddings, index_name):
    vectorstore = PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings,
    )
    return vectorstore.as_retriever(
        search_type="similarity", 
        search_kwargs={"k": 5}
    )
