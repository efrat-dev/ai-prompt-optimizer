import os
from pathlib import Path

class Config:
    # OpenAI settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.1
    
    # File paths
    BASE_DIR = Path(__file__).parent
    PROMPT_FILE = BASE_DIR / "prompt.md"
    
    # Gradio settings
    SERVER_NAME = "0.0.0.0"
    SERVER_PORT = 7860
    SHARE = False
    DEBUG = True
    
    # App settings
    APP_TITLE = "AI Prompt Optimizer"
    APP_DESCRIPTION = "Transform your casual questions into professional, optimized prompts for better AI responses"