"""
State Definition
"""

from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

class State(TypedDict):
    messages: Annotated[list, add_messages]
    business_description: str
    business_location: str
    context_types_and_justifications: dict[str, str]
    raw_contexts: dict[str, str]
    contexts: dict[str, str]
    ad_copies: list[dict]
