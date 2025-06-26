import json
from openai import OpenAI
from config import Config
from prompt_manager import PromptManager

# Emoji constants
ERROR_EMOJI = "\u274c"      # ❌
SUCCESS_EMOJI = "\u2705"    # ✅
WARNING_EMOJI = "\u26a0"    # ⚠️

class OpenAIClient:
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.client = None
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
    
    def generate_optimized_prompt(self, user_message):
        """Generate optimized prompt from user message"""
        if not user_message.strip():
            return "Please enter a message"
        
        if not self.api_key:
            return self._get_api_key_error_message()
        
        try:
            system_prompt = PromptManager.load_system_prompt()
            
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            result = response.choices[0].message.content.strip()
            return self._parse_response(result)
            
        except Exception as e:
            return self._get_api_error_message(str(e))
    
    def check_api_key(self):
        """Check if API key is set and working"""
        if not self.api_key:
            return f"{ERROR_EMOJI} OPENAI_API_KEY not set"
        
        try:
            # Test with a minimal request
            self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=1
            )
            return f"{SUCCESS_EMOJI} API key is working!"
        except Exception as e:
            return f"{ERROR_EMOJI} API Error: {str(e)}"
    
    def _parse_response(self, result):
        """Parse JSON response and extract markdown"""
        try:
            parsed = json.loads(result)
            if "markdown" in parsed:
                return parsed["markdown"]
            else:
                return result
        except json.JSONDecodeError:
            return result
    
    def _get_api_key_error_message(self):
        return f"""{ERROR_EMOJI} **OpenAI API Key Missing**
To use this tool, you need to set your OpenAI API key as an environment variable.
**How to set it:**
1. Get your API key from https://platform.openai.com/api-keys
2. Set the environment variable:
   - Linux/Mac: `export OPENAI_API_KEY='your-key-here'`
   - Windows: `set OPENAI_API_KEY=your-key-here`
3. Restart this application
**Alternative:** You can also create a `.env` file with:
```
OPENAI_API_KEY=your-key-here
```"""
    
    def _get_api_error_message(self, error):
        return f"""{ERROR_EMOJI} **Error occurred:**
{error}
**Common solutions:**
1. Check your internet connection
2. Verify your OpenAI API key is valid
3. Ensure you have sufficient API credits
4. Try again in a few moments"""
