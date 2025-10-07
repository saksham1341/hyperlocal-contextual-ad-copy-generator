"""
Project Configurations
"""

from os import getenv

def _confirm_existence_and_get(key: str) -> str:
    """
    Confirm that an environment variable exists and return it's value.
    
    Args:
        key: The environment variable to get.
    """
    
    _ = getenv(key, None)
    if _ is None:
        raise RuntimeError(f"`{key}` not found in the environment.")
    
    return _

GOOGLE_API_KEY = _confirm_existence_and_get("GOOGLE_API_KEY")

SERPER_API_KEY = _confirm_existence_and_get("SERPER_API_KEY")
SERPER_TBS = getenv("SERPER_TBS", "qdr:w")  # Date range of search, past week by default.

POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL = getenv("POTENTIAL_CONTEXT_TYPE_GENERATOR_MODEL", "gemini-2.5-pro")
FETCH_CONTEXTS_MODEL = getenv("FETCH_CONTEXTS_MODEL", "gemini-2.5-pro")
