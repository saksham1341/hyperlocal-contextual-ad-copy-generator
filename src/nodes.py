"""
Graph Nodes
"""

from config import AD_COPY_GENERATOR_MODEL, FETCH_CONTEXTS_MODEL, POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL
import json
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import ToolMessage
from src import prompts, schemas
from src.models import get_model
from src.state import State
from src.tools import search_internet

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
    
    chain = prompt | model.langchain_model
    
    response = chain.invoke(
        input={
            "format_instructions": parser.get_format_instructions(),
            "business_description": business_description
        }
    )
    
    return {
        "messages": [response],
        "context_types_and_justifications": parser.parse(response.content).context_types_and_justifications
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
    model = get_model(FETCH_CONTEXTS_MODEL)
    tools = [search_internet]
    model_with_tools = model.langchain_model.bind_tools(tools)
    prompt = prompts.FetchContextsPrompt
    parser = PydanticOutputParser(pydantic_object=schemas.FetchedContextsOutput)
    
    chain = prompt | model_with_tools
    response = chain.invoke(
        input={
            "format_instructions": parser.get_format_instructions(),
            "business_description": state["business_description"],
            "business_location": state["business_location"],
            "context_types": list(state["context_types_and_justifications"].keys()),
            "raw_contexts": state.get("raw_contexts", None)
        }
    )
    
    try:
        contexts = parser.parse(response.content).contexts
    except:
        contexts = None
    
    return {
        "messages": [response],
        "contexts": contexts
    }

def raw_context_compiler(state: State) -> dict:
    """
    Compile the results of tool calls into the state.raw_contexts object.
    """
    
    messages = state.get("messages")
    raw_contexts = {}
    
    for message in reversed(messages):
        if not isinstance(message, ToolMessage):
            break
        
        tool_response = json.loads(message.content)
        raw_contexts[tool_response["context_type"]] = tool_response["results"]
    
    return {
        "raw_contexts": raw_contexts,
    }

def generate_ad_copies(state: State) -> dict:
    business_description = state["business_description"]
    business_location = state["business_location"]
    contexts = state["contexts"]
    
    model = get_model(AD_COPY_GENERATOR_MODEL)
    prompt = prompts.AdCopyGenerationPrompt
    parser = PydanticOutputParser(pydantic_object=schemas.AdCopyGeneratorOutput)
    
    chain = prompt | model | parser
    response = chain.invoke(
        input={
            "business_description": business_description,
            "business_location": business_location,
            "contexts": json.dumps(contexts),
            "format_instructions": parser.get_format_instructions()
        }
    )
    
    return {
        "ad_copies": response.ad_copies
    }

if __name__ == "__main__":
    state = State(
        business_description="A merchandise store which makes custom merch on trending memes.",
        business_location="Noida, Uttar Pradesh, India",
    )
    
    state["context_types_and_justifications"] = generate_potential_context_types(state)["context_types_and_justifications"]
    print(fetch_contexts(state))
