import random
import time


def show_banner() -> None:
    print("================================================")
    print("Q & A session about Python coding conventions")
    print("Attendees: User, ChatGPT\n")
    print("(c) 2026, babaksoft")
    print("================================================\n")


def exists_collection() -> bool:
    return False


def init_collection() -> None:
    print("[INFO] Initializing...")
    delay = random.uniform(1.0, 3.0)
    time.sleep(delay)
    print("[INFO] Knowledge base successfully initialized.")


def query_llm(question: str) -> str:
    print("\n[INFO] Asking question from ChatGPT...")
    delay = random.uniform(1.0, 3.0)
    time.sleep(delay)
    return "(Answer to user question)"


def init_qa_loop() -> None:
    running = True
    while running:
        print("Ask a question about Python coding conventions (enter q to quit)")
        question = input("[User]:\n")
        if question.lower() != "q":
            answer = query_llm(question)
            print(f"\n[ChatGPT]:\n{answer}\n")
        else:
            print("\nThanks for being a guest in this Q & A session. See you soon!")
            running = False


def main():
    show_banner()
    print("[INFO] Checking document ingestion status...")
    if not exists_collection():
        print("[INFO] Document not yet ingested. Processing...")
        init_collection()
    else:
        print("[INFO] Document already ingested.")

    init_qa_loop()


if __name__ == "__main__":
    main()
