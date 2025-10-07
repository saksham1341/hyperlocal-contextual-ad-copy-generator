"""
Graph Nodes
"""

from config import POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL
from src import prompts, schemas
from src.models import get_model
from src.state import State

def generate_potential_context_types(state: State) -> dict:
    """
    Fetch the business description from the state and
    generate context types the business can
    potentially capitalize on.
    """
    
    business_description = state["business_description"]
    model = get_model(POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL)
    langchain_model = model.langchain_model.with_structured_output(schema=schemas.GeneratedPotentialContextTypesOutput)
    
    response = langchain_model.invoke(
        input=prompts.GeneratePotentialContextTypesPrompt.invoke(
            input={
                "business_description": business_description
            }
        )
    )
    
    return {
        "context_types_and_justifications": response.context_types_and_justifications
    }

if __name__ == "__main__":
    state = State(
        business_description="A merchandise store which makes custom merch on trending memes."
    )
    
    print(generate_potential_context_types(state))
