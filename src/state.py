"""
State Definition
"""

from typing_extensions import TypedDict

class State(TypedDict):
    business_description: str
    business_location: str
    context_types_and_justifications: dict[str, str]
    contexts: dict[str, str]
