# GenAI Lab project

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https://github.com/babaksoft/genai-lab/raw/refs/heads/master/pyproject.toml)
![Static Badge](https://img.shields.io/badge/type-GenAI-orange)
![Static Badge](https://img.shields.io/badge/platform-OpenAI-orange)
![Static Badge](https://img.shields.io/badge/framework-llamaindex-orange)
![Static Badge](https://img.shields.io/badge/framework-langchain-orange)
![GitHub License](https://img.shields.io/github/license/babaksoft/genai-lab)

## Small demos (before cleanup)

Currently experimenting with LLM frameworks, OpenAI only. Started with LangChain but,
due to issues with LangSmith platform, switched to LlamaIndex. Proceeding with Llama.

### `core` package

Simple experiments using test prompts and samples to explore LLM capabilities.

- API: OpenAI

Can be run in two modes :
- Demo script (assistant_demo.py)
- Simple CLI tool, powered by `click` (assistant_cli.py)

### Basic LLM chat

Playing with sync and async, as well as multimodal, chat calls

- API: LlamaIndex
- Run mode: Standalone script (chat_demo.py)
- Sample output: No

### `rag` package: Demonstrating basic RAG

Designed a simple RAG experiment to chat about PEP-8 (inspired by an excellent tutorial on
[Real Python](https://www.realpython.com))

- API: LlamaIndex (planned)
- Run mode: Standalone script (rag_simple.py)

### `dialog` package: Demonstrating a short conversation about France

Basic experiment with token counts, latency and consistency

- API: LangChain
- Run mode: Standalone script (dialog_demo.py)
- Sample output: Yes

### `planner` package: Demonstrating a simple agent

Tired of demo Calculator tools, designed a simple TODO database and related tools to challenge my first agent.

- API: LlamaIndex
- Run mode: Standalone script (planner_demo.py)
- Sample output: Yes
- Pending: Ask agent to make a weekly plan, based on task priorities and 8 hr/day schedule

