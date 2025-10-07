"""
Model Schemas for structured data processing.
"""

from pydantic import BaseModel, Field

class GeneratedPotentialContextTypesOutput(BaseModel):
    context_types_and_justifications: dict[str, str] = Field(..., description="A dictionary which maps a context type to it's justification.")
