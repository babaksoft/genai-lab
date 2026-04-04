"""
CLI (Command Line Interface) tool that exposes several Gen AI commands
supported by Assistant class.
"""

from os import PathLike

import click

from genai_lab.core.assistant import Assistant

assistant = Assistant()


@click.group(help="Convenient shortcuts for common AI agent tasks.")
def cli():
    pass


@cli.command(
    help="Summarizes given file into bullet list format with limited word count."
)
@click.option(
    "--file",
    "-f",
    help="A text file whose content should be summarized (20,000 characters max.)",
)
@click.option(
    "--max-words",
    "-w",
    default=100,
    help="Maximum number of words in file content summary (default : 100)",
)
def shorten(file: str | PathLike, max_words: int = 100):
    summary = assistant.summarize_file(file, max_words)
    word_count = len(summary.split(" "))
    print(f"\nSummary :\n{summary}")
    print(f"\nSummary text has {word_count} words.")


@cli.command(help="Detects sentiment in a given user review.")
@click.option(
    "--review",
    "-r",
    help="User review whose sentiment should be detected (20,000 characters max.)",
)
def sentiment(review: str):
    ai_sentiment = assistant.get_sentiment(review)
    print(f"Sentiment : {ai_sentiment}")


@cli.command(help="Detects a fixed set of moods in a given user text.")
@click.option(
    "--text",
    "-t",
    help="User text whose mood should be detected (20,000 characters max.)",
)
def mood(text: str):
    ai_mood = assistant.get_mental_state(text)
    print(f"Mood : {ai_mood}")


@cli.command(
    help="Translates a given text to a target language."
    " Source language is auto-detected."
)
@click.option(
    "--text",
    "-t",
    help="Text that should be translated (2000 characters max.)",
)
@click.option(
    "--to-lang",
    "-l",
    default="English",
    help="Target language for translation (default : English)",
)
def translate(text: str, to_lang: str = "English"):
    translated = assistant.translate(text, to_lang)
    print(f"{to_lang.title()} translation :\n{translated}")


@cli.command(help="Rewrites given text with a new tone.")
@click.option(
    "--text",
    "-t",
    help="Text that should be adapted to a new tone (2000 characters max.)",
)
@click.option(
    "--context",
    "-c",
    default="business",
    help="Context or tone that given text should be adapted to."
    " Supported contexts : business, official, friendly, childish (default : business)",
)
def adapt(text: str, context: str = "business"):
    adapted = assistant.change_tone(text, context)
    print(f"Adapted to {context.lower()} tone :\n{adapted}")


@cli.command(
    help="Provides detailed explanation for a technical IT-related" " error message."
)
@click.option(
    "--message",
    "-m",
    help="Error message that should be explained (2000 characters max.)",
)
@click.option(
    "--context",
    "-c",
    default="Unknown",
    help="Optional context for error message "
    "(example : I'm installing program X on my MacBook).",
)
@click.option(
    "--max-words",
    "-w",
    default=200,
    help="Maximum number of words in error explanation (default : 200)",
)
def explain(message: str, context: str = "Unknown", max_words: int = 200):
    explained = assistant.explain_error(message, context, max_words)
    print(f"AI Explanation :\n{explained}")


if __name__ == "__main__":
    cli()
