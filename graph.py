"""
Main LangGraph Module
"""

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from pprint import pprint
from src.nodes import generate_potential_context_types, fetch_contexts, raw_context_compiler, generate_ad_copies
from src.state import State
from src.tools import search_internet, search_news, search_places

graph_builder = StateGraph(
    state_schema=State,
)

graph_builder.add_node("generate_potential_context_types", generate_potential_context_types)
graph_builder.add_node("fetch_contexts", fetch_contexts)
graph_builder.add_node("tools", ToolNode(tools=[search_internet, search_news, search_places]))
graph_builder.add_node("raw_context_compiler", raw_context_compiler)
graph_builder.add_node("generate_ad_copies", generate_ad_copies)

def tools_condition_end_redirector(redirect_to: str):
    """
    A wrapper around the builtin tools_condition
    to redirect it's END output to some other node, 
    without showing up in the graph.
    """
    
    def _(state: State) -> str:
        res = tools_condition(state)
        if res == END:
            res = redirect_to
        
        return res
    
    return _

graph_builder.add_edge(START, "generate_potential_context_types")
graph_builder.add_edge("generate_potential_context_types", "fetch_contexts")
graph_builder.add_conditional_edges(
    "fetch_contexts",
    tools_condition_end_redirector("generate_ad_copies"),
    {
        "tools": "tools",
        "generate_ad_copies": "generate_ad_copies"
    }
)
graph_builder.add_edge("tools", "raw_context_compiler")
graph_builder.add_edge("raw_context_compiler", "fetch_contexts")
graph_builder.add_edge("generate_ad_copies", END)

graph = graph_builder.compile()
with open("graph.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

resp = graph.stream({
    "business_description": "A merchandise store which makes custom merch on trending memes.",
    "business_location": "Noida, Uttar Pradesh, India",
}, stream_mode="values")

waiting_for = ["context_types_and_justifications", "raw_contexts", "contexts", "ad_copies"]
for x in resp:
    if waiting_for and x.get(waiting_for[0], False):
        print()
        print("=" * 50)
        print(f"GENERATED {waiting_for[0]}")
        print()
        pprint(x[waiting_for[0]])
        print()
        
        waiting_for = waiting_for[1:]
