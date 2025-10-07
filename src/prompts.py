"""
Prompts for the LLMs.
"""

from langchain_core.prompts import PromptTemplate

GeneratePotentialContextTypesPrompt = PromptTemplate(
    template="""
You are an expert marketing strategist specializing in hyper-local, contextual advertising. Your primary skill is identifying real-world, dynamic conditions that can be used to create timely and relevant marketing messages.

Your task is to analyze the following business description and generate a concise list of "context types" that this business could use for its ad campaigns. These context types must be categories of data that can realistically be fetched for a given location using APIs or other real-time data sources.

For each context type you identify, provide a brief, one-sentence justification for why it is relevant to this specific business.

Business Description:
{business_description}

Do not write ad copy. Only provide the list of context types and their justifications.

Example for a business described as "A quiet bookstore with an in-house cafe serving artisanal coffee and pastries":

Weather: Perfect for promoting the cozy cafe with a hot coffee on a rainy day, or the cool, air-conditioned reading space on a hot day.

Time of Day: Ads can target the morning commute for coffee, lunchtime for a quick bite and read, or evenings for a relaxing place to unwind.

Local Events: Can advertise as a quiet escape from a noisy nearby festival or a convenient meeting spot for conference attendees.

Air Quality Index (AQI): On days with poor air quality, the store can be promoted as a "clean air oasis" for reading and relaxing indoors.
""",
    input_variables=["business_description"]
)
