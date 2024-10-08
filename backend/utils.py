from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os

GOOGLE_MODELS = [
    ""
]

OPENAI_MODELS = [
    ""
]

NVIDIA_NIM_MODELS = [
    ""
]

GROQ_MODELS = [
    ""
]

def create_llm(model_name: str, **kwargs):
    if model_name in GOOGLE_MODELS:
        return ChatGoogleGenerativeAI(model=model_name,
                                      api_key=os.getenv("GEMINI_API_KEY"),
                                      **kwargs)

    elif model_name in OPENAI_MODELS:
        return ChatOpenAI(model=model_name,
                          api_key = os.getenv("OPENAI_API_KEY"),
                          **kwargs)
    
    elif model_name in NVIDIA_NIM_MODELS:
        return ChatNVIDIA(model=model_name,
                          api_key=os.getenv("NVIDIA_API_KEY"),
                          **kwargs)
    
    elif model_name in GROQ_MODELS:
        return ChatGroq(model=model_name,
                        api_key=os.getenv("GROQ_API_KEY"),
                        **kwargs)
    else:
        raise Exception(f"Invalid model name - {model_name}")

