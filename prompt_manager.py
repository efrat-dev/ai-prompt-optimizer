from config import Config

class PromptManager:
    DEFAULT_SYSTEM_PROMPT = """You are an AI prompt optimization specialist. Your task is to transform casual user questions into professional, well-structured prompts that will generate better AI responses.
When given a user's casual question or request, you should:
1. Analyze the intent and context
2. Structure it with clear instructions
3. Add relevant context or constraints
4. Make it more specific and actionable
5. Format it professionally
Return your response as a JSON object with a "markdown" field containing the optimized prompt in markdown format.
Example:
Input: "How to learn programming?"
Output: {"markdown": "# Learning Programming Effectively\\n\\n## Objective\\nProvide a comprehensive guide for learning programming from beginner to intermediate level.\\n\\n## Requirements\\n- Include specific learning paths\\n- Recommend resources and tools\\n- Provide timeline estimates\\n- Address common challenges\\n\\n## Context\\nAssume the learner has no prior programming experience and wants practical, actionable advice.\\n\\nPlease structure your response with clear headings and actionable steps."}"""
    
    @staticmethod
    def load_system_prompt():
        """Load system prompt from prompt.md file"""
        try:
            if Config.PROMPT_FILE.exists():
                content = Config.PROMPT_FILE.read_text(encoding='utf-8').strip()
                return content if content else PromptManager.DEFAULT_SYSTEM_PROMPT
            else:
                return PromptManager.DEFAULT_SYSTEM_PROMPT
        except Exception as e:
            print(f"Error loading prompt.md: {e}")
            return PromptManager.DEFAULT_SYSTEM_PROMPT
    
    @staticmethod
    def check_prompt_file():
        """Check if prompt.md file exists and is readable"""
        if Config.PROMPT_FILE.exists():
            try:
                content = Config.PROMPT_FILE.read_text(encoding='utf-8').strip()
                if content:
                    return "✅ prompt.md file found and loaded"
                else:
                    return "⚠️ prompt.md file is empty, using default prompt"
            except Exception as e:
                return f"⚠️ Error reading prompt.md: {e}"
        else:
            return "⚠️ prompt.md not found, using default prompt"