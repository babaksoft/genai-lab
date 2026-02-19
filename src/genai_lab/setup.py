import os

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]


def get_completion(
    prompt,
    model="gpt-4o-mini",
    temperature=0,
    max_output_tokens=100
):
    """ Get completion for a single prompt (str) or a chat (list[dict]) """
    response = client.responses.create(
        input=prompt,
        model=model,
        max_output_tokens=max_output_tokens,
        temperature=temperature
    )

    return response.output[0].content[0].text
