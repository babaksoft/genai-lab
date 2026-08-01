# Generative AI Laboratory

Experimenting with Generative AI ideas using `LlamaIndex` (and, maybe later, `LangChain`)

## Progressive demo for a useful LlamaAgents workflow

**Goal**

Assessing different LLM capabilities with benchmark scripts

**Objectives**

* Provide working sample code for most features in Workflows API
* Implement a non-trivial workflow step-by-step
* Implement LLM-as-a-Judge pattern, with a strong model as the judge LLM (local or inexpensive cloud)
* Implement basic observability via logging and Arize Phoenix
* Use chain-of-thought reasoning, when appropriate

**Main parameters**

- Judge LLM (frontier or frontier-like)
  * Cloud model : OpenAI (e.g., gpt-5.6) using credits
  * AWS Bedrock model : Easily configured frontier
  * Ollama model, local : Gemma4
  * Ollama model, cloud : gpt-oss:120b-cloud
- Candidate LLMs
  * All local Ollama models (with timed-out start/stop logic)
  * All cloud Ollama models
  * Selected OpenAI models, using credits
  * Selected AWS Bedrock models

**Branching logic**

Handle model types differently

**Example**

For local Ollama models : Run models using runtime CLI execution (running `ollama run model` from Python process), wait a specified amount for the model to load, then call the model.