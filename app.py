"""
Streamlit App
"""

import streamlit as st

_ = st.navigation([
    "pages/index.py",
    "pages/generator.py"
], position="hidden")
_.run()
