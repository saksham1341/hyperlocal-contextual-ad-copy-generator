"""
Landing page.
"""

import streamlit as st
from github_link_component import github_link

github_link("https://github.com/saksham1341/hyperlocal-contextual-ad-copy-generator")
st.title("Hyperlocal Contextual Ad-Copy Generator")
st.text("Stop Guessing. Know Your Audience Instantly.")

st.markdown("""
A **Streamlit-powered application** that creates **hyperlocal, context-aware ad copy** using a **LangGraph workflow** and **Google Gemini** models.
Built for marketers, growth teams, and developers who want to automate the creation of personalized ad creatives tailored to specific locations and contextual signals.

## What This Project Does

* Generates **contextual, creative ad copy** using Gemini.
* Uses **LangGraph** to orchestrate graph-based reasoning steps.
* Offers an **interactive Streamlit UI** for input, generation, and visualization.
* Provides **modular prompt templates** and customizable nodes.
* Includes a **visual workflow graph** (`graph.png`) to illustrate the generation pipeline.

---
""")

if st.button(
    label="Go to Generator",
    key="go-to-ad-copy-generator",
):
    st.switch_page("pages/generator.py")