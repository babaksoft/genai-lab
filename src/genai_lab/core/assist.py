from ..config import config
from ..prompts.assist_prompts import SUMMARY_PROMPT, SENTIMENT_PROMPT
from ..prompts.assist_prompts import MENTAL_STATE_PROMPT
from ..setup import get_completion

def summarize_text(
    text: str,
    delimiter=config.DELIMITER,
    max_words=config.MAX_WORDS,
    max_input_len = config.MAX_INPUT_LEN,
    model: str=config.DEF_GPT_MODEL,
    debug=False) -> str:
    """ Uses given GPT model to summarize input text into bullet list format.
    If input text is longer than expected, it will be truncated to configured
    maximum value. """

    if not text:
        raise ValueError("The value of 'text' parameter cannot be None or an empty string.")

    text = text.replace("\n", " ").strip()
    if len(text) > max_input_len:
        text = text[:max_input_len]

    max_tokens = int(max_words * 4. / 3)  # simple approximation
    prompt = SUMMARY_PROMPT.format(
        delimiter=delimiter, max_words=max_words, text=text)
    if debug:
        print(f"Input prompt :\n{prompt}")
    response = get_completion(prompt, model=model, max_output_tokens=max_tokens)

    return response


def summarize_file(
    path,
    delimiter=config.DELIMITER,
    max_words=config.MAX_WORDS,
    max_input_len = config.MAX_INPUT_LEN,
    model: str=config.DEF_GPT_MODEL) -> str | None:
    """ Uses given GPT model to summarize contents of given text file
    into bullet list format. If text content is longer than expected,
    the rest of file contents will be truncated. Raises error if given
    file is binary, invalid or inaccessible. """

    try:
        with open(path, "r") as file:
            text = file.read()

        summary = summarize_text(
            text, delimiter=delimiter, max_words=max_words,
            max_input_len=max_input_len, model=model)
        return summary
    except Exception as ex:
        print(f"[ERROR] {ex}")


def summarize_demo():
    sample_file = config.SAMPLES_DIR / "portman-bio.txt"
    summary = summarize_file(sample_file, max_words=100)
    word_count = len(summary.split(" "))
    print(f"\nSummary :\n{summary}")
    print(f"\nSummary text has {word_count} words.")


def detect_sentiment(
    review: str,
    delimiter: str=config.DELIMITER,
    max_input_len: int=config.MAX_INPUT_LEN,
    model: str=config.DEF_GPT_MODEL
) -> str | None:
    """ Uses given GPT model to detect sentiment in a user-supplied review. """

    if not review:
        raise ValueError(
            "[ERROR] Value for 'review' cannot be None or empty string.")

    input_len = len(review)
    if input_len > max_input_len:
        print(f"[WARN] This feature accepts maximum length of {max_input_len}"
              f" for user review, but a review with length {input_len} "
              f"was given.\nLong reviews will be truncated.")
        review = review[:max_input_len]

    prompt = SENTIMENT_PROMPT.format(
        delimiter=delimiter, review=review
    )
    response = get_completion(
        prompt, model=model, max_output_tokens=20
    )

    return response


def sentiment_demo():
    review_1 = config.SAMPLE_REVIEW_1
    sentiment_1 = "Positive"
    sentiment = detect_sentiment(review_1)
    correct = sentiment == sentiment_1
    print(review_1)
    print(f"Sentiment : {sentiment} ({'Correct' if correct else 'Incorrect'})")

    review_2 = config.SAMPLE_REVIEW_2
    sentiment_2 = "Negative"
    sentiment = detect_sentiment(review_2)
    correct = sentiment == sentiment_2
    print(review_2)
    print(f"Sentiment : {sentiment} ({'Correct' if correct else 'Incorrect'})")


def classify_mental_state(
    statement: str,
    delimiter: str=config.DELIMITER,
    max_input_len: int=config.MAX_INPUT_LEN,
    model: str=config.DEF_GPT_MODEL
) -> str | None:
    """ Uses given GPT model to classify mental state from a user-supplied statement. """

    if not statement:
        raise ValueError(
            "[ERROR] Value for 'statement' cannot be None or empty string.")

    input_len = len(statement)
    if input_len > max_input_len:
        print(f"[WARN] This feature accepts maximum length of {max_input_len}"
              f" for user statement, but a statement with length {input_len} "
              f"was given.\nLong statements will be truncated.")
        statement = statement[:max_input_len]

    prompt = MENTAL_STATE_PROMPT.format(
        delimiter=delimiter, statement=statement
    )
    response = get_completion(
        prompt, model=model, max_output_tokens=20
    )

    return response


def mental_state_demo():
    statement_1 = config.SAMPLE_STATEMENT_1
    state_1 = "Depression"
    state = classify_mental_state(statement_1)
    correct = state == state_1
    print(statement_1)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")

    statement_2 = config.SAMPLE_STATEMENT_2
    state_2 = "Suicidal"
    state = classify_mental_state(statement_2)
    correct = state == state_2
    print(statement_2)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")

    statement_3 = config.SAMPLE_STATEMENT_3
    state_3 = "Anxiety"
    state = classify_mental_state(statement_3)
    correct = state == state_3
    print(statement_3)
    print(f"Mental State : {state} ({'Correct' if correct else 'Incorrect'})")


if __name__ == "__main__":
    mental_state_demo()
