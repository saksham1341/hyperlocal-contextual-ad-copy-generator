"""
State Definition
"""

from typing_extensions import TypedDict

class State(TypedDict):
    business_description: str
    business_location: str
    context_types: list[str]
    contexts: dict[str, str]
