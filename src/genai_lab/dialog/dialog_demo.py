from datetime import datetime

import numpy as np
import tiktoken
from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings

from genai_lab.dialog.env_setup import init

init()

ENCODING_NAME = "o200k_base"
MODEL_NAME = "gpt-4o-mini"
DIALOG = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep your answers concise.",
    },
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
]

MESSAGES = [
    "What are the official states in France?",
    "Which state is a better place to live in?",
]

encoding = tiktoken.encoding_for_model(MODEL_NAME)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def show_banner():
    print("\n===================================================================")
    print("Simple conversation demo using LangChain and GPT models")
    print("Objective: Inspect token usage, latency and response consistency")
    print(f"\nModel: {MODEL_NAME}")
    print("===================================================================\n")


def count_tokens(dialog):
    num_tokens = 0
    for message in dialog:
        num_tokens += (
            4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        )
        num_tokens += len(encoding.encode(message["content"]))
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens


def cosine_similarity(vec_u: list[float], vec_v: list[float]) -> float:
    """Calculate the cosine similarity between two vectors."""
    u = np.array(vec_u)
    v = np.array(vec_v)
    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))


def consistency_score(responses: list[str]) -> float:
    """Calculate a consistency score for a list of responses."""
    embeds = [embeddings.embed_query(response) for response in responses]
    similarities = []
    for i in range(len(embeds)):
        for j in range(i + 1, len(embeds)):
            sim = cosine_similarity(embeds[i], embeds[j])
            similarities.append(sim)
    return np.mean(similarities)


def ask_model(chat_model, message, dialog):
    dialog.append({"role": "user", "content": message})

    print("Current dialog:")
    print(f"Token count (input, estimated): {count_tokens(dialog)}")

    start = datetime.now()
    response = chat_model.invoke(dialog)
    elapsed = datetime.now() - start
    dialog.append({"role": "assistant", "content": response.content})

    print("[User]:\n" + message + "\n")
    print("[GPT]:\n" + response.content + "\n")
    print(f"Token count (total, estimated): {count_tokens(dialog)}")
    print("Token count (actual):")
    print(f"  Input:  {response.usage_metadata["input_tokens"]}")
    print(f"  Output: {response.usage_metadata["output_tokens"]}")
    print(f"  Total:  {response.usage_metadata["total_tokens"]}")
    print(f"Latency: {str(elapsed)}\n")

    return response.content, elapsed.total_seconds()


def main():
    show_banner()
    model = init_chat_model(MODEL_NAME, temperature=0.0, max_tokens=1000)
    q1_responses = []
    q2_responses = []
    latencies = []
    for i in range(3):
        curr_dialog = DIALOG.copy()
        print(f"=== Iteration {i + 1} ===")
        q1_response, latency = ask_model(model, MESSAGES[0], curr_dialog)
        q1_responses.append(q1_response)
        latencies.append(latency)
        q2_response, latency = ask_model(model, MESSAGES[1], curr_dialog)
        q2_responses.append(q2_response)
        latencies.append(latency)

    print("\n=== Consistency Scores ===")
    print(f"Message : {MESSAGES[0]}")
    print(f"LLM Response Consistency: {consistency_score(q1_responses):.4f}")
    print(f"Message : {MESSAGES[1]}")
    print(f"LLM Response Consistency: {consistency_score(q2_responses):.4f}")
    print(f"\nAverage Latency: {np.mean(latencies):.4f}")


if __name__ == "__main__":
    main()
