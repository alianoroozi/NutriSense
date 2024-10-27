import os
import time
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from app.config import (
    PINECONE_INDEX_NAME, 
    EMBEDDING_DIMENSION, 
    PINECONE_API_KEY, 
    PINECONE_REGION
)


if __name__ == "__main__":

    load_dotenv()
    
    pc = Pinecone(api_key=PINECONE_API_KEY)

    cloud = PINECONE_API_KEY
    region = PINECONE_REGION
    spec = ServerlessSpec(cloud=cloud, region=region)

    index_name = PINECONE_INDEX_NAME
    embedding_dimension = EMBEDDING_DIMENSION


    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=embedding_dimension,
            metric="cosine",
            spec=spec
        )
        # Wait for index to be ready
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)

    # See that it is empty
    print("Index before upsert:")
    print(pc.Index(index_name).describe_index_stats())
    print("\n")