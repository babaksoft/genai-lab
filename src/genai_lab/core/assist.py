from ..config import config
from ..prompts.assist_prompts import SUMMARY_PROMPT
from ..setup import get_completion

def summarize_text(
    text: str,
    delimiter=config.DELIMITER,
    max_words=config.MAX_WORDS,
    max_chars_in = config.MAX_CHARS_IN,
    model: str=config.DEF_GPT_MODEL,
    debug=False) -> str:
    """ Uses given GPT model to summarize input text into bullet list format.
    If input text is longer than expected, it will be truncated to configured
    maximum value. """

    if not text:
        raise ValueError("The value of 'text' parameter cannot be None or an empty string.")

    text = text.replace("\n", " ").strip()
    if len(text) > max_chars_in:
        text = text[:max_chars_in]

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
    max_chars_in = config.MAX_CHARS_IN,
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
            max_chars_in=max_chars_in, model=model)
        return summary
    except Exception as ex:
        print(f"[ERROR] {ex}")


def summarize_demo():
    sample_file = config.SAMPLES_DIR / "portman-bio.txt"
    summary = summarize_file(sample_file, max_words=100)
    word_count = len(summary.split(" "))
    print(f"\nSummary :\n{summary}")
    print(f"\nSummary text has {word_count} words.")

if __name__ == "__main__":
    summarize_demo()
