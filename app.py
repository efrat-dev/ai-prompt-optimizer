import gradio as gr
from config import Config
from openai_client import OpenAIClient
from status_checker import StatusChecker
from ui_components import UIComponents

def create_app():
    """Create and configure the Gradio app"""
    openai_client = OpenAIClient()
    status_checker = StatusChecker()
    
    with gr.Blocks(title=Config.APP_TITLE) as demo:
        # Header
        UIComponents.create_header()
        
        # Status section
        status_display, refresh_btn = UIComponents.create_status_section()
        
        # Main interface
        user_input, submit_btn, output = UIComponents.create_main_interface()
        
        # Examples
        UIComponents.create_examples(user_input)
        
        # Instructions
        UIComponents.create_instructions()
        
        # Event handlers
        demo.load(
            lambda: status_checker.get_status_report(),
            outputs=status_display
        )
        
        refresh_btn.click(
            lambda: status_checker.get_status_report(),
            outputs=status_display
        )
        
        submit_btn.click(
            openai_client.generate_optimized_prompt,
            inputs=user_input,
            outputs=output
        )
    
    return demo

def main():
    """Main function to run the app"""
    demo = create_app()
    demo.launch(
        server_name=Config.SERVER_NAME,
        server_port=Config.SERVER_PORT,
        share=Config.SHARE,
        debug=Config.DEBUG
    )

if __name__ == "__main__":
    main()