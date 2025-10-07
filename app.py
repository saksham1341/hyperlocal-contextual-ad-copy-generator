"""
Streamlit App
"""

from graph import graph_builder
import streamlit as st

st.title("Hyperlocal Contextual Ad Copy Generator")
st.text("Stop writing generic ads. Create marketing that connects with customers by using AI to instantly weave today's local conditions into your promotions.")
st.divider()

st.subheader("Enter a brief description of your business")
st.text_area(
    label="Enter a brief description of your business",
    placeholder="e.g., A merchandise store which makes custom merch on trending memes.",
    key="business_description",
    label_visibility="hidden"
)

if not st.session_state.get("business_description", ""):
    st.button(
        label="Submit"
    )
    st.stop()
    
st.subheader("Enter the location of your business")
st.text_area(
    label="Enter the location of your business",
    placeholder="e.g., Noida, Uttar Pradesh, India",
    key="business_location",
    label_visibility="hidden"
)
if not st.session_state.get("business_location", ""):
    st.button(
        label="Submit"
    )
    st.stop()

graph = graph_builder.compile()
stream = graph.stream(
    input={
        "business_description": st.session_state["business_description"],
        "business_location": st.session_state["business_location"]
    },
    stream_mode="values",
)

_ = st.empty()
with _.status(label="Generating potential context types."):
    while True:
        state = next(stream)
        if state.get("context_types_and_justifications"):
            break
_.empty()

st.divider()

st.subheader("Potential Context Types Identified")
st.text("Here are the types of context I will search for and the justification behind them")
for context_type, justification in state.get("context_types_and_justifications").items():
    st.markdown(f"**{context_type}**")
    st.markdown(f"{justification}")

_ = st.empty()
with _.status(label="Fetching context data.") as X:
    found_raw_context = False
    while True:
        state = next(stream)
        if not found_raw_context and state.get('raw_contexts'):
            found_raw_context = True
            X.update(label="Fetched raw context data, synthesizing now.")
        if state.get("contexts"):
            break
_.empty()

st.divider()

st.subheader("Context Fetched for Ad creation")
st.text("Here is the information I found related to different contexts.")
for context_type, context in state.get("contexts").items():
    st.markdown(f"**{context_type}**")
    st.markdown(f"{context}")

_ = st.empty()
with _.status(label="Generating Ad Copies."):
    while True:
        state = next(stream)
        if state.get("ad_copies"):
            break
_.empty()

st.divider()

st.subheader("Ad Copies Generated")
st.text("I have generated some Ad copies using the found contexts.")
for idx, ad_copy in enumerate(state.get("ad_copies")):
    st.markdown(f"### Ad Set {idx + 1}")
    st.markdown(f"**Content**")
    st.markdown(f"{ad_copy.content}")
    st.markdown(f"**Contexts Used:**")
    st.markdown(f"{', '.join(list(ad_copy.contexts.keys()))}")
