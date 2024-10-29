# NutriSense
Provides smart and sensible dietary nutrition advice.


# NutriSense

NutriSense is an AI-driven question-answering assistant providing smart and sensible dietary nutrition advice. Using advanced language models and a knowledge base from the *Encyclopedia of Human Nutrition*, NutriSense answers questions on nutrition, aiding users with reliable, evidence-based information.

## Key Features
- **Retrieval-Augmented Generation (RAG)**: NutriSense uses RAG to search and retrieve relevant nutrition information from an encyclopedia knowledge base.
- **OpenAI Language Model**
- **LangChain**: LangChain constructs and manages the chain used for retrieval and response generation.
- **Pinecone**: Efficiently stores and retrieves embeddings of text chunks from the knowledge base.
- **Flask API**
- **GitHub Actions & AWS EC2 Deployment**: Docker image is automatically pushed to AWS ECR and deployed to an EC2 instance through GitHub Actions for seamless CI/CD.

## Application Structure
- **Knowledge Base**: The *Encyclopedia of Human Nutrition* PDF located in the `docs/` directory.
- **Index Creation**: `scripts/init_pinecone.py` initializes a Pinecone index.
- **Database Population**: `scripts/populate_db.py` reads the PDF, chunks the content, and stores the embeddings in the Pinecone index.
- **API Server**: A Flask server provides an API to interact with the NutriSense app.

## Runnning the App Locally
Make sure to set the following env variables before running the app locally:
- OPENAI_API_KEY
- LANGCHAIN_API_KEY
- PINECONE_API_KEY
- PINECONE_CLOUD
- PINECONE_REGION

