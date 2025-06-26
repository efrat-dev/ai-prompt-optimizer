import gradio as gr
from config import Config

class UIComponents:
    @staticmethod
    def create_header():
        """Create app header"""
        gr.Markdown(f"# 🚀 {Config.APP_TITLE}")
        gr.Markdown(Config.APP_DESCRIPTION)
    
    @staticmethod
    def create_status_section():
        """Create status display section"""
        with gr.Row():
            with gr.Column():
                status_display = gr.Markdown()
                refresh_btn = gr.Button("🔄 Refresh Status", size="sm")
        return status_display, refresh_btn
    
    @staticmethod
    def create_main_interface():
        """Create main input/output interface"""
        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(
                    label="Enter your question or prompt",
                    placeholder="Example: Are there programming languages that only have recursion and no loops?",
                    lines=4
                )
                submit_btn = gr.Button("✨ Optimize Prompt", variant="primary")
            
            with gr.Column():
                output = gr.Textbox(
                    label="Optimized Prompt",
                    lines=15,
                    show_copy_button=True
                )
        return user_input, submit_btn, output
    
    @staticmethod
    def create_examples(user_input):
        """Create examples section"""
        examples = [
            ["Are there programming languages that only have recursion and no loops?"],
            ["Who earns more money, a data scientist or a full-stack developer?"],
            ["How to learn programming effectively?"],
            ["What are the best practices for API design?"],
            ["Explain machine learning to a beginner"]
        ]
        gr.Examples(examples=examples, inputs=user_input)
    
    @staticmethod
    def create_instructions():
        """Create instructions section"""
        gr.Markdown("""
        ## 📋 Setup Instructions
        
        1. **Set your OpenAI API key:**
           - Get your key from [OpenAI Platform](https://platform.openai.com/api-keys)
           - Set environment variable: `export OPENAI_API_KEY='your-key-here'`
        
        2. **Optional: Create custom prompt.md file**
           - Create a `prompt.md` file in the root directory
           - Add your custom system prompt for the optimizer
           - If not provided, a default prompt will be used
        
        3. **Enter your question and click "Optimize Prompt"**
        
        ## 🎯 How it works
        This tool analyzes your casual question and returns a structured, professional prompt that will help you get better responses from AI models.
        """)