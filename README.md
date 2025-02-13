# LLM Chatbot with FastAPI

This is a chatbot project built using **FastAPI** and **Poetry**. It is designed to handle LLM (Large Language Models)
chat functionality, with support for real-time APIs.

## Features

- FastAPI for API development
- Support for AI chat using LLM (LangChain, OpenAI)
- Poetry for dependency management
- Testing with `pytest`

## Setup and Usage

### Prerequisites

- Python 3.12 or higher
- Poetry installed

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd llm_learning
   ```

2. Install dependencies with `poetry`:

   ```bash
   poetry install
   ```

3. Run the FastAPI server:

   ```bash
   poetry run uvicorn api.main:app --host <your_host> --port <your_port_number> --reload
   ```

4. Visit the API at `http://<your_host>:<your_port_number>` in your browser.

### Testing

Run the tests:

```bash
poetry run pytest
```

### Export Libraries

## Contributing

Feel free to fork the repository and submit improvements through pull requests. Feedback is always welcome!
