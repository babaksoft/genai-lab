import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from openai.types.responses import ResponseOutputMessage, ResponseOutputText

from genai_lab.config import config

_ = load_dotenv(find_dotenv())  # read local .env file
client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]


def get_completion(
    prompt: str,
    model: str = config.DEF_GPT_MODEL,
    temperature: float = 0,
    max_output_tokens: int = 100,
) -> str:
    """Get completion for a single prompt (str) or a chat (list[dict])"""
    # return "Try prompt in ChatGPT Web UI"  # Temporary stub
    response = client.responses.create(
        input=prompt,
        model=model,
        max_output_tokens=max_output_tokens,
        temperature=temperature,
    )

    output: ResponseOutputMessage = response.output[0]
    content: ResponseOutputText = output.content[0]
    return content.text
