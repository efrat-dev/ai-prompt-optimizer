# 🔧 AI Prompt Optimizer - Development Documentation

This document contains technical information for developers who want to understand, modify, or contribute to the AI Prompt Optimizer project.

## 📁 Project Structure

```
ai-prompt-optimizer/
├── app.py                 # Main application entry point
├── config.py             # Configuration settings
├── openai_client.py      # OpenAI API client
├── prompt_manager.py     # Prompt file management
├── status_checker.py     # System status monitoring
├── ui_components.py      # Gradio UI components
├── requirements.txt      # Python dependencies
├── prompt.md            # Custom system prompt (optional)
├── .env                 # Environment variables (create this)
├── README.md            # User guide
└── DEVELOPMENT.md       # This file
```

## 🏗️ Architecture Overview

The application follows a modular architecture with clear separation of concerns:

### Module Descriptions

- **`app.py`**: Main application file that creates and launches the Gradio interface
- **`config.py`**: Centralized configuration management
- **`openai_client.py`**: Handles OpenAI API interactions and error handling
- **`prompt_manager.py`**: Manages system prompt loading and validation
- **`status_checker.py`**: Monitors API connectivity and system status
- **`ui_components.py`**: Modular Gradio UI component definitions

## 🔧 API Reference

### OpenAIClient

The `OpenAIClient` class handles all interactions with the OpenAI API.

```python
client = OpenAIClient()

# Generate optimized prompt
result = client.generate_optimized_prompt("How to learn Python?")

# Check API key status
status = client.check_api_key()
```

#### Methods

- `__init__()`: Initializes the client with API key from config
- `generate_optimized_prompt(user_message)`: Main method to generate system prompts
- `check_api_key()`: Validates API key connectivity
- `_parse_response(result)`: Parses JSON response and extracts markdown
- `_get_api_key_error_message()`: Returns formatted error message for missing API key
- `_get_api_error_message(error)`: Returns formatted error message for API errors

### StatusChecker

The `StatusChecker` class monitors system health and API connectivity.

```python
checker = StatusChecker()

# Get complete status report
report = checker.get_status_report()

# Get individual status checks
api_status = checker.get_api_status()
prompt_status = checker.get_prompt_file_status()
```

#### Methods

- `__init__()`: Initializes with OpenAI client
- `get_api_status()`: Returns API key connectivity status
- `get_prompt_file_status()`: Returns prompt.md file status
- `get_overall_status()`: Returns overall system readiness
- `get_status_report()`: Returns formatted status report with timestamp
- `_get_current_time()`: Returns current timestamp

### PromptManager

The `PromptManager` class handles system prompt loading and management.

```python
# Load system prompt from prompt.md or use default
system_prompt = PromptManager.load_system_prompt()

# Check prompt file status
status = PromptManager.check_prompt_file()
```

#### Methods

- `load_system_prompt()`: Loads custom prompt from prompt.md or returns default
- `check_prompt_file()`: Validates prompt.md file existence and readability

#### Constants

- `DEFAULT_SYSTEM_PROMPT`: Fallback prompt when prompt.md is not available

### UIComponents

The `UIComponents` class contains modular Gradio UI component definitions.

```python
# Create header section
UIComponents.create_header()

# Create status monitoring section
status_display, refresh_btn = UIComponents.create_status_section()

# Create main input/output interface
user_input, submit_btn, output = UIComponents.create_main_interface()
```

#### Methods

- `create_header()`: Creates app title and description
- `create_status_section()`: Creates status display and refresh button
- `create_main_interface()`: Creates input field, submit button, and output area
- `create_examples(user_input)`: Creates example prompts section
- `create_instructions()`: Creates setup and usage instructions

### Config

The `Config` class centralizes all application configuration.

```python
from config import Config

# Access configuration values
api_key = Config.OPENAI_API_KEY
model = Config.OPENAI_MODEL
port = Config.SERVER_PORT
```

#### Configuration Categories

**OpenAI Settings:**
- `OPENAI_API_KEY`: API key from environment
- `OPENAI_MODEL`: Model to use (default: "gpt-3.5-turbo")
- `MAX_TOKENS`: Maximum response tokens (default: 1000)
- `TEMPERATURE`: Response creativity (default: 0.1)

**File Paths:**
- `BASE_DIR`: Application base directory
- `PROMPT_FILE`: Path to prompt.md file

**Gradio Settings:**
- `SERVER_NAME`: Server binding address (default: "0.0.0.0")
- `SERVER_PORT`: Server port (default: 7860)
- `SHARE`: Enable public sharing (default: False)
- `DEBUG`: Enable debug mode (default: True)

**App Settings:**
- `APP_TITLE`: Application title
- `APP_DESCRIPTION`: Application description

## 🔄 Application Flow

1. **Initialization** (`app.py`):
   - Load configuration
   - Initialize OpenAI client
   - Create status checker
   - Build Gradio interface

2. **Status Check** (`status_checker.py`):
   - Verify API key connectivity
   - Check prompt.md file availability
   - Display overall system status

3. **User Input Processing** (`openai_client.py`):
   - Receive user question
   - Load system prompt template
   - Send request to OpenAI API
   - Parse and return optimized prompt

4. **UI Updates** (`ui_components.py`):
   - Display results in output area
   - Update status indicators
   - Handle user interactions

## 🧪 Development Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- Git

### Local Development

1. **Clone and Setup**:
```bash
git clone https://github.com/efrat-dev/ai-prompt-optimizer.git
cd ai-prompt-optimizer
pip install -r requirements.txt
```

2. **Configure Environment**:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

3. **Run in Development Mode**:
```bash
python app.py
```

The application will run with `DEBUG=True` and auto-reload on file changes.

### Testing API Integration

```python
# Test OpenAI connectivity
from openai_client import OpenAIClient
client = OpenAIClient()
print(client.check_api_key())

# Test prompt generation
result = client.generate_optimized_prompt("Test question")
print(result)
```

### Custom Prompt Development

Create and test custom system prompts:

1. Create `prompt.md` with your template
2. Test with various input types
3. Validate JSON response format
4. Check token limits (80 tokens max for system prompts)

## 🤝 Contributing

### Code Style

- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to all public methods
- Keep functions focused and modular

### Adding New Features

1. **Create Feature Branch**:
```bash
git checkout -b feature/your-feature-name
```

2. **Implement Changes**:
   - Add new functionality in appropriate modules
   - Update configuration if needed
   - Add error handling
   - Test thoroughly

3. **Update Documentation**:
   - Update this development guide
   - Update user README if needed
   - Add code comments

4. **Submit Pull Request**:
   - Include description of changes
   - List any breaking changes
   - Add testing instructions

### Testing Guidelines

- Test all API interactions with various inputs
- Verify error handling for edge cases
- Test UI components in different browsers
- Validate configuration changes
- Test with and without prompt.md file

### Common Development Tasks

**Adding New UI Components**:
```python
# In ui_components.py
@staticmethod
def create_new_component():
    """Create new UI component"""
    # Implementation here
    return component
```

**Adding New Configuration Options**:
```python
# In config.py
class Config:
    # Add new configuration option
    NEW_OPTION = os.getenv('NEW_OPTION', 'default_value')
```

**Extending OpenAI Client**:
```python
# In openai_client.py
def new_api_method(self, parameter):
    """New API interaction method"""
    try:
        # Implementation
        return result
    except Exception as e:
        return self._get_api_error_message(str(e))
```

## 🐛 Debugging

### Common Development Issues

**Import Errors**:
- Check Python path and virtual environment
- Verify all dependencies are installed
- Check for circular imports

**API Connection Issues**:
- Verify API key is correctly set
- Check internet connectivity
- Test with minimal API request

**UI Issues**:
- Check Gradio version compatibility
- Test component interactions
- Verify event handler bindings

### Logging

Enable detailed logging for debugging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Monitoring

Monitor API response times and token usage:

```python
import time
start_time = time.time()
# API call
duration = time.time() - start_time
print(f"API call took {duration:.2f} seconds")
```

## 📝 Release Process

1. **Version Bump**: Update version in relevant files
2. **Testing**: Run comprehensive tests
3. **Documentation**: Update user and developer docs
4. **Changelog**: Document all changes
5. **Tag Release**: Create Git tag
6. **Deploy**: Update deployment if applicable

## 🔗 External Dependencies

### Required Libraries

- **gradio**: Web interface framework
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management

### API Dependencies

- **OpenAI API**: Core functionality for prompt optimization
- **Internet Connection**: Required for API calls

## 📊 Performance Considerations

- **Token Limits**: System prompts limited to 80 tokens
- **Rate Limiting**: OpenAI API has rate limits
- **Memory Usage**: Minimal memory footprint
- **Response Time**: Typically 1-3 seconds per request

---

For user-facing documentation, see [README.md](README.md)
