from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

def setup_faiss(domain_documents):
    """Loads documents, generates embeddings, and initializes FAISS."""
    documents = TextLoader(domain_documents).load()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
