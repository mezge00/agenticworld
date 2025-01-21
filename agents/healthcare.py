from utils.faiss_setup import setup_faiss
from utils.gemini_wrapper import GoogleGeminiLLM

def create_healthcare_agent(domain_documents):
    faiss_store = setup_faiss(domain_documents)

    def tool_func(input_text):
        retriever = faiss_store.as_retriever()
        docs = retriever.get_relevant_documents(input_text)
        context = " ".join([doc.page_content for doc in docs[:3]])  # Top 3 docs
        gemini_llm = GoogleGeminiLLM()
        return gemini_llm.call(input_text, context)

    return tool_func
def get_healthcare_insights(input_text, domain_documents="agents/data/healthcare_documents.txt"):
    healthcare_agent = create_healthcare_agent(domain_documents)
    return healthcare_agent(input_text)
