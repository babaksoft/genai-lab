import asyncio

from dotenv import load_dotenv
from llama_index.core.llms import ChatMessage, TextBlock, ImageBlock
from llama_index.llms.openai import OpenAI

load_dotenv()

GPT_MODEL = "gpt-4o-mini"
g_llm = OpenAI(model=GPT_MODEL)


def simple_chat():
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="Explain Generative AI in 100 words or less."),
    ]

    stream_resp = g_llm.stream_chat(messages)
    for token in stream_resp:
        print(token.delta, end="", flush=True)


async def asimple_chat():
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What does 'TL;DR' means in Web lingo?"),
    ]

    stream_resp = await g_llm.astream_chat(messages)
    async for token in stream_resp:
        print(token.delta, end="", flush=True)


def multimodal_chat():
    messages = [
        ChatMessage(
            role="user",
            blocks=[
                ImageBlock(path="./chart.png"),
                TextBlock(text="Describe the image in 100 words or less."),
            ]
        )
    ]
    response = g_llm.chat(messages)

    print("Response from LLM:")
    print(str(response))
    print("LLM response (content):")
    print(response.message.content)


if __name__ == "__main__":
    multimodal_chat()
