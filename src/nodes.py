"""
Graph Nodes
"""

from config import POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL
from langchain_core.output_parsers import PydanticOutputParser
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
    prompt = prompts.GeneratePotentialContextTypesPrompt
    parser = PydanticOutputParser(pydantic_object=schemas.GeneratedPotentialContextTypesOutput)
    
    chain = prompt | model.langchain_model | parser
    
    response = chain.invoke(
        input={
            "format_instructions": parser.get_format_instructions(),
            "business_description": business_description
        }
    )
    
    return {
        "context_types_and_justifications": response.context_types_and_justifications
    }

def fetch_contexts(state: State) -> dict:
    """
    Use tool calling to fetch required contexts for current state.
    """
    
    # TODO:
    # define a web search tool
    # create the tool enabled model
    # write a FetchContextsOutput schema
    # run the FetchContextsPrompt with proper format instructions
    pass

if __name__ == "__main__":
    state = State(
        business_description="A merchandise store which makes custom merch on trending memes."
    )
    
    print(generate_potential_context_types(state))
