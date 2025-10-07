"""
LLM Models
"""

from config import GOOGLE_API_KEY
from langchain_core.language_models import BaseLanguageModel
from langchain_google_genai import ChatGoogleGenerativeAI


class BaseLLMModel:
    """
    Abstract LLM Model class.
    """
    
    langchain_model: BaseLanguageModel

model_dict: dict[str, type] = {}

def get_model(key: str) -> BaseLLMModel:
    if key not in model_dict:
        raise RuntimeError(f"Model `{key}` not found!")
    
    return model_dict[key]()
    
class Gemini25Pro(BaseLLMModel):
    """
    Gemini 2.5 Pro
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.langchain_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            google_api_key=GOOGLE_API_KEY,
        )

model_dict["gemini-2.5-pro"] = Gemini25Pro

class Gemini25Flash(BaseLLMModel):
    """
    Gemini 2.5 Flash
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.langchain_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=GOOGLE_API_KEY,
        )

model_dict["gemini-2.5-flash"] = Gemini25Flash

class Gemini25FlashLite(BaseLLMModel):
    """
    Gemini 2.5 Flash Lite
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.langchain_model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=GOOGLE_API_KEY,
        )

model_dict["gemini-2.5-flash-lite"] = Gemini25FlashLite
