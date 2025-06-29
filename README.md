# 🚀 AI Prompt Optimizer

Transform your casual questions into professional, domain-specific **system prompts** for better AI responses.

## 🎯 What is a System Prompt?

A **system prompt** is a set of instructions that defines how an AI should behave, what expertise it should demonstrate, and what constraints it should follow when responding to user queries. Think of it as giving the AI a professional role and specific guidelines before it answers your question.

## 🔬 How This Tool Works

This application analyzes your casual question and generates a tailored **system prompt** that:

- **Defines the AI's Role**: Assigns relevant expertise (e.g., "computer science teaching assistant", "clinical nutritionist")
- **Sets Professional Tone**: Ensures responses are precise and domain-appropriate  
- **Adds Constraints**: Specifies what to avoid (e.g., speculation, overly simplistic answers)
- **Provides Context**: Includes the relevant knowledge domain and expected output format
- **Focuses the Response**: Narrows the AI's focus to the most relevant aspects of your topic

## 💡 Why Use System Prompts?

Instead of getting generic answers, you get responses from an AI that "knows" it should act as a subject matter expert in the specific field your question relates to. This results in:

- More accurate and detailed information
- Professionally structured responses
- Domain-specific terminology and context
- Focused answers that avoid irrelevant tangents

**Example:** Instead of asking "What is recursion?" and getting a general answer, the tool creates a system prompt that makes the AI respond as a computer science instructor, ensuring technical accuracy and appropriate depth.

## Example Workflow

**Input:**
```
How to learn programming?
```

**Output:**
```markdown
### You are a programming instructor. Provide guidance on learning programming effectively, emphasizing key strategies and resources. Avoid vague or overly simplistic advice.

**Example:**  
- `Start with basic concepts like variables and loops before moving to more complex topics.`

**Category:** `Programming Education`
```

## ✨ Features

- **Smart Prompt Optimization**: Transforms casual questions into structured, professional prompts
- **Real-time Status Monitoring**: Shows API connectivity and system status
- **Interactive Web Interface**: Clean, user-friendly Gradio interface
- **Custom System Prompts**: Support for custom prompt templates via `prompt.md`
- **Built-in Examples**: Pre-configured examples to get started quickly
- **Error Handling**: Comprehensive error handling and user feedback

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- OpenAI API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/efrat-dev/ai-prompt-optimizer.git
cd ai-prompt-optimizer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your-openai-api-key-here
```

### Step 4: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:7860` (default port configured in `config.py`)

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |

### Configuration Options (config.py)

```python
# OpenAI settings
OPENAI_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 80
TEMPERATURE = 0.1

# Server settings
SERVER_NAME = "0.0.0.0"
SERVER_PORT = 7860
SHARE = False
DEBUG = True
```

## 🚀 Usage

1. **Access the Application**: Open your browser and navigate to `http://localhost:7860` (or the port configured in `config.py`)

2. **Check Status**: The status section shows:
   - API key connectivity
   - Prompt file status
   - Overall system readiness

3. **Enter Your Question**: Type your casual question or prompt in the input field

4. **Optimize**: Click "✨ Optimize Prompt" to generate a professional version

5. **Copy Result**: Copy button to copy the optimized prompt, and use it.

### Built-in Examples

The application includes several pre-configured examples:

1. "Are there programming languages that only have recursion and no loops?"
2. "Who earns more money, a data scientist or a full-stack developer?"
3. "How to learn programming effectively?"
4. "What are the best practices for API design?"
5. "Explain machine learning to a beginner"

## 🐛 Troubleshooting

### Common Issues

**API Key Error:**
- Ensure your OpenAI API key is correctly set
- Check that you have sufficient API credits
- Verify the API key has the necessary permissions

**Application Won't Start:**
- Check Python version (3.8+ required)
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify port 7860 is available (or change SERVER_PORT in config.py)
- Check if another process is using the same port

### Status Indicators

- 🟢 **Ready to use**: All systems operational
- 🟡 **Partially ready**: Some features may be limited
- 🔴 **API key required**: OpenAI API key needs to be configured

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Gradio Documentation](https://gradio.app/docs)
- [Get OpenAI API Key](https://platform.openai.com/api-keys)
- [Development Documentation](DEVELOPMENT.md) - For developers and contributors
