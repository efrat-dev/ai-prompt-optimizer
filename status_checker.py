from openai_client import OpenAIClient
from prompt_manager import PromptManager

class StatusChecker:
    def __init__(self):
        self.openai_client = OpenAIClient()
    
    def get_api_status(self):
        """Get API key status"""
        return self.openai_client.check_api_key()
    
    def get_prompt_file_status(self):
        """Get prompt file status"""
        return PromptManager.check_prompt_file()
    
    def get_overall_status(self):
        """Get overall app status"""
        api_status = self.get_api_status()
        prompt_status = self.get_prompt_file_status()
        
        if "✅" in api_status and ("✅" in prompt_status or "⚠️" in prompt_status):
            return "🟢 Ready to use!"
        elif "❌" in api_status:
            return "🔴 API key required"
        else:
            return "🟡 Partially ready"
    
    def get_status_report(self):
        """Get complete status report"""
        api_status = self.get_api_status()
        prompt_status = self.get_prompt_file_status()
        overall_status = self.get_overall_status()
        
        return f"""
**Overall Status:** {overall_status}
**API Status:** {api_status}
**Prompt File Status:** {prompt_status}
---
*Status checked at: {self._get_current_time()}*
        """
    
    def _get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

