"""
State Definition
"""

from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

def update_raw_context(left, right):
    if not isinstance(left, dict):
        left = {}
    if not isinstance(right, dict):
        right = {}
    
    left.update(right)
    
    return left

class State(TypedDict):
    messages: Annotated[list, add_messages]
    business_description: str
    business_location: str
    context_types_and_justifications: dict[str, str]
    raw_contexts: Annotated[dict[str, dict], update_raw_context]
    contexts: dict[str, str]
