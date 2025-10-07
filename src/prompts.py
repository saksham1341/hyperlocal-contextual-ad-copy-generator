"""
Prompts for the LLMs.
"""

from langchain_core.prompts import PromptTemplate

GeneratePotentialContextTypesPrompt = PromptTemplate(
    template="""
You are an expert marketing strategist. Your task is to analyze the business description to identify potential context types that can be used for hyper-local, contextual ad campaigns, and provide a clear justification for why each context type is relevant to the business.

Follow the instructions below to format your response.
{format_instructions}

Business Description:
{business_description}
""",
    input_variables=["business_description", "format_instructions"]
)
