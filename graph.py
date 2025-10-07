"""
Main LangGraph Module
"""

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from src.nodes import generate_potential_context_types, fetch_contexts, raw_context_compiler
from src.state import State
from src.tools import search_internet

graph_builder = StateGraph(
    state_schema=State,
)

graph_builder.add_node("generate_potential_context_types", generate_potential_context_types)
graph_builder.add_node("fetch_contexts", fetch_contexts)
graph_builder.add_node("tools", ToolNode(tools=[search_internet]))
graph_builder.add_node("raw_context_compiler", raw_context_compiler)

def fetch_contexts_tool_router(state: State) -> str:
    _ = tools_condition(state)
    
    return _

graph_builder.add_edge(START, "generate_potential_context_types")
graph_builder.add_edge("generate_potential_context_types", "fetch_contexts")
graph_builder.add_conditional_edges(
    "fetch_contexts",
    fetch_contexts_tool_router,
    {
        "tools": "tools",
        END: END
    }
)
graph_builder.add_edge("tools", "raw_context_compiler")
graph_builder.add_edge("raw_context_compiler", "fetch_contexts")

graph = graph_builder.compile()
with open("temp.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

resp = graph.stream({
    "business_description": "A merchandise store which makes custom merch on trending memes.",
    "business_location": "Noida, Uttar Pradesh, India",
})

for x in resp:
    print(x)
