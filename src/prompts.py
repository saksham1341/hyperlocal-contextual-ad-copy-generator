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

FetchContextsPrompt = PromptTemplate(
    template="""
You are an autonomous research agent specializing in hyper-local market intelligence. Your mission is to gather real-time, localized data based on a set of specified context types and consolidate your findings into a final JSON object.

You will execute the following process:
1.  **Analyze the Inputs**: You will be given a business description, a location, and a JSON array of context types to investigate. Use the business description to better understand what kind of information would be most relevant.
2.  **Iterate and Research**: For EACH context type in the provided list, you must formulate a precise search query and use the available `search_internet` tool to find the most current and relevant information for the specified location.
3.  **Synthesize Findings**: After you have executed searches for all the required context types and have received the output of tool calls, you will process all the gathered information.
4.  **Final Output**: Your final answer MUST be a single, well-formed JSON object.

If you cannot find relevant information for a specific context type after searching, the value should be a string indicating that, such as "No significant local events found at this time."

Follow the instructions below to format your response.
{format_instructions}

Here are your inputs:
- **Business Description**: `{business_description}`
- **Business Location**: `{business_location}`
- **Context Types to Research**: `{context_types}`
- **Output of Tool Calls**:
{raw_contexts}
""",
    input_variables=["format_instructions", "business_description", "business_location", "context_types", "raw_contexts"]
)
