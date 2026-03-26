# ruff: noqa: F403, F405

from textwrap import wrap

from ..config import config
from ..config.samples import *
from .assistant import Assistant

assistant = Assistant(debug=True)


def summarize_demo():
    sample_file = config.SAMPLES_DIR / "portman-bio.txt"
    summary = assistant.summarize_file(sample_file, max_words=100)
    word_count = len(summary.split(" "))
    print(f"\nSummary :\n{summary}")
    print(f"\nSummary text has {word_count} words.")


def sentiment_demo():
    review_1 = SAMPLE_REVIEW_1
    sentiment_1 = "Positive"
    sentiment = assistant.get_sentiment(review_1)
    correct = sentiment == sentiment_1
    print(review_1)
    print(f"Sentiment : {sentiment} ({'Correct' if correct else 'Incorrect'})")

    review_2 = SAMPLE_REVIEW_2
    sentiment_2 = "Negative"
    sentiment = assistant.get_sentiment(review_2)
    correct = sentiment == sentiment_2
    print(review_2)
    print(f"Sentiment : {sentiment} ({'Correct' if correct else 'Incorrect'})")


def mental_state_demo():
    statement_1 = SAMPLE_STATEMENT_1
    state_1 = "Depression"
    state = assistant.get_mental_state(statement_1)
    correct = state == state_1
    print(statement_1)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")

    statement_2 = SAMPLE_STATEMENT_2
    state_2 = "Suicidal"
    state = assistant.get_mental_state(statement_2)
    correct = state == state_2
    print(statement_2)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")

    statement_3 = SAMPLE_STATEMENT_3
    state_3 = "Anxiety"
    state = assistant.get_mental_state(statement_3)
    correct = state == state_3
    print(statement_3)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")


def translate_demo():
    trans_1 = assistant.translate(SAMPLE_TEXT_1, to_lang="French")
    lines = wrap(trans_1, width=80)
    trans_1 = "\n".join(lines)

    print(f"Original text :{SAMPLE_TEXT_1}\n")
    print(f"Translation (Google) :{SAMPLE_TRANS_1}\n")
    print("Translation (GPT) :")
    print(trans_1)

    trans_2 = assistant.translate(SAMPLE_TEXT_2, to_lang="English")
    lines = wrap(trans_2, width=80)
    trans_2 = "\n".join(lines)

    print(f"\nGoogle text (Italian) :{SAMPLE_TEXT_2}\n")
    print(f"Original text :{SAMPLE_TRANS_2}\n")
    print("Translation (GPT) :")
    print(trans_2)


def rewrite_demo():
    # # Polite refusal letter to a hiring manager
    sample_mail = SAMPLE_MAIL_1
    context = "Business"
    response = assistant.change_tone(sample_mail, context=context)
    print(f"\nOriginal mail :\n{sample_mail}")
    print(f"New context : {context}")
    print("\nAdapted mail (from LLM) :")
    print(response)

    # Polite letter someone writes to ask why their visa was declined
    sample_mail = SAMPLE_MAIL_2
    context = "Official"
    response = assistant.change_tone(sample_mail, context=context)
    print(f"\nOriginal mail :\n{sample_mail}")
    print(f"New context : {context}")
    print("\nAdapted mail (from LLM) :")
    print(response)

    # A casual mail with an invalid context LLM is expected to reject
    # (but it doesn't!)
    sample_mail = SAMPLE_MAIL_3
    context = "Flirtatious"
    response = assistant.change_tone(sample_mail, context=context)
    print(f"\nOriginal mail :\n{sample_mail}")
    print(f"New context : {context}")
    print("\nAdapted mail (from LLM) :")
    print(response)


def explain_demo():
    err_message = SAMPLE_ERROR_1
    context = "I'm building a Visual Studio 2022 solution with C# .NET 8.0 compiler."
    response = assistant.explain_error(message=err_message, context=context)

    print(f"\nError message :\n{err_message}")
    print(f"Context : {context}")
    print("\nExplanation (from LLM) :")
    print(response)

    err_message = SAMPLE_ERROR_2
    response = assistant.explain_error(message=err_message)
    context = None

    print(f"\nError message :\n{err_message}")
    print(f"Context : {context}")
    print("\nExplanation (from LLM) :")
    print(response)


if __name__ == "__main__":
    rewrite_demo()
