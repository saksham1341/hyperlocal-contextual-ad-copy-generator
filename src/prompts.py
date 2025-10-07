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

AdCopyGenerationPrompt = PromptTemplate(
    template="""
You are an expert copywriter and marketing strategist specializing in hyper-local, contextual advertising. Your mission is to write three distinct, short, and punchy ad copy variations for a business by creatively integrating a set of real-time, local data.

**Your Inputs:**
* **Business Details:**
    * Description: `{business_description}`
    * Location: `{business_location}`
* **Contextual Data:** A JSON object of real-time conditions at the business location.
    * `{contexts}`

**Your Creative Instructions:**
1.  **Weave, Don't Just State:** Do not just plainly state the context (e.g., "It's sunny"). Instead, creatively weave the contextual data into the ad's narrative to create a sense of urgency, relevance, or opportunity. The connection must feel smart and natural.
2.  **Connect Context to Benefit:** Each ad must connect a specific context directly to a problem the business solves or a benefit it offers. For example, connect "rainy weather" to the "cozy atmosphere" of a cafe.
3.  **Localize:** Mention the location (`{business_location}`) in each ad to make it feel personal and directly relevant to the reader.
4.  **Distinct Angles:** Generate three unique variations. They should explore different tones (e.g., humorous, urgent, comforting) or focus on different contexts if multiple are provided.
5.  **Call to Action (CTA):** End each ad with a clear and compelling Call to Action.

**Your Output Format Instructions:**
You MUST format your response as a single, valid JSON object that strictly follows the instructions below.
{format_instructions}

---

**Now, generate the ad copy for the inputs provided.**    
""",
    input_variables=["business_description", "business_location", "contexts", "format_instructions"],
)
