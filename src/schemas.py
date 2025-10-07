"""
Model Schemas for structured data processing.
"""

from pydantic import RootModel, BaseModel, Field

class GeneratedPotentialContextTypesOutput(BaseModel):
    context_types_and_justifications: dict[str, str] = Field(description="A dictionary which maps a context type to it's justification.")

class FetchedContextsOutput(BaseModel):
    contexts: dict[str, str] = Field(description="A dictionary which a context type to the final actual context.")

class AdCopy(BaseModel):
    content: str = Field(description="The content of the ad.")
    contexts: dict[str, str] = Field(description="The contexts used for this ad.")

class AdCopyGeneratorOutput(BaseModel):
    ad_copies: list[AdCopy] = Field(description="A list of generated ad copies")
