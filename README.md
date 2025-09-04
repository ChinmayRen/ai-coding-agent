# AI Coding Agent

This project is a command-line AI coding agent that leverages the Google Gemini API to understand and execute coding-related tasks. The agent can interact with the local filesystem within a designated working directory.

## Features

- **File System Operations:** The agent can list files, read file contents, and write to files.
- **Code Execution:** The agent can execute Python scripts.
- **Extensible Tools:** The agent's capabilities are defined by a set of clear "tool" functions that can be expanded.
- **Configurable:** The agent's working directory can be configured.

## How It Works

The agent takes a natural language prompt from the command line. It uses the Gemini model with a system prompt that instructs it to create a plan and use the available tools to fulfill the user's request. The agent and the model then engage in a loop of function calling and response generation until the task is complete or no further actions can be taken.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd ai-coding-agent
    ```

2.  **Install dependencies:**
    This project uses `pyproject.toml` to manage dependencies. You can install them using `pip`:
    ```bash
    pip install .
    ```
    This will install `google-genai` and `python-dotenv`.

3.  **Set up environment variables:**
    The agent requires a Google Gemini API key.
    -   Create a file named `.env` in the project root.
    -   Add your API key to the file, like so:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
    You can get an API key from the [Google AI Studio](https://aistudio.google.com/).

## Usage

Run the agent from the command line, passing your request as a string argument.

```bash
python main.py "Your request here"
```

For example:
```bash
python main.py "List all the files in the current directory"
```

### Verbose Mode

To see more details about the agent's operations, including token counts and function call details, use the `--verbose` flag:

```bash
python main.py "Your request here" --verbose
```

## Available Tools

The agent has access to the following functions:

-   `get_files_info(path='.')`: Lists files and directories at the given path.
-   `get_file_content(file_path)`: Reads and returns the content of a specified file.
-   `run_python_file(file_path, args=[])`: Executes a Python file with optional arguments.
-   `write_file(file_path, content)`: Writes or overwrites a file with the provided content.

## Configuration

The agent's working directory is defined in `config.py`. By default, it is set to `./calculator`. All file operations are restricted to this directory for security.

```python
# config.py
WORKING_DIR = "./calculator"
```

## Future Steps

To make the agent more powerful and conversational, the following features could be implemented:

1.  **Session Memory (Interactive Mode):** The agent could run in a continuous loop (a REPL: Read-Eval-Print Loop) that accepts user input, processes it, and waits for the next command. It should remember the full history of the current conversation.
2.  **Long-Term Memory (History Saving):** The agent could save the conversation history to a file when a session ends and load this history when it starts up again. This would allow the agent to maintain context across multiple sessions.