from agents.financial import create_financial_agent
from agents.healthcare import create_healthcare_agent
from agents.legal import create_legal_agent
from agents.education import create_education_agent
from agents.market_insights import create_market_insights_agent
import gradio as gr

def initialize_agents():
    financial_agent = create_financial_agent("E:/Bus/skills/financial_documents.txt")
    healthcare_agent = create_healthcare_agent("E:/Bus/skills/healthcare_documents.txt")
    legal_agent = create_legal_agent("E:/Bus/skills/legal_documents.txt")
    education_agent = create_education_agent("E:/Bus/skills/education_documents.txt")
    market_insights_agent = create_market_insights_agent("E:/Bus/skills/market_documents.txt")

    def central_agent(input_text):
        agents = [financial_agent, healthcare_agent, legal_agent, education_agent, market_insights_agent]
        results = []
        for agent in agents:
            try:
                response = agent(input_text)
                if response:
                    results.append(response)
            except Exception as e:
                print(f"Error: {e}")
        return "\n\n".join(results) if results else "No suitable agent could answer your query."

    return central_agent

def create_interface(agent):
    def handle_query(input_text):
        return agent(input_text)

    return gr.Interface(
        fn=handle_query,
        inputs="text",
        outputs="text",
        title="Multi-Agent AI System",
        description="Interact with specialized agents for healthcare, finance, legal, and more."
    )

if __name__ == "__main__":
    central_agent = initialize_agents()
    interface = create_interface(central_agent)
    interface.launch()
