# ruff: noqa: F403, F405

from os import PathLike

from ..setup import get_completion
from ..config import config
from ..prompts.assist_prompts import *
from .assistant_utils import TextParam, validate_params, clean_text

_model = config.DEF_GPT_MODEL
_delimiter = config.DELIMITER


class Assistant:
    """
    Demonstrates generic capabilities of a GPT model.

    Parameters
    -----------
    model : str
        Specific flavor of openAI GPT model to use. Default is "gpt-4o-mini".

    delimiter : str
        Delimiter to use for preventing prompt injection. Default is 4 consecutive back-ticks (i.e. ````).

    debug : bool
        Used to show constructed prompt before submitting to GPT model. Default is False.
    """

    def __init__(
        self, model: str = _model, delimiter: str = _delimiter, debug: bool = False
    ):
        self.model = model
        self.delimiter = delimiter
        self.debug = debug

    @staticmethod
    def _get_token_count(words: int) -> int:
        return int(words * 4.0 / 3)

    @staticmethod
    def _get_word_count(tokens: int) -> int:
        return int(tokens * 3.0 / 4)

    @validate_params([TextParam(name="text")])
    def summarize(self, text: str, max_words: int = config.MAX_WORDS) -> str:
        """Uses GPT model to summarize input text into bullet list format.

        If input text is longer than expected, it will be truncated to default max length (20,000 characters).

        Parameters
        ----------
        text : str
            Text to summarize into bullet list.

        max_words : int
            Maximum number of words for summary text. Default is 100 words.

        Returns
        -------
        summary : str
            Input text summarized into bullet list.
        """

        text = text.replace("\n", " ").strip()
        if len(text) > config.MAX_INPUT_L:
            text = text[: config.MAX_INPUT_L]

        max_tokens = int(max_words * 4.0 / 3)  # simple approximation
        prompt = SUMMARY_PROMPT.format(
            delimiter=self.delimiter, max_words=max_words, text=text
        )
        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(
            prompt, model=self.model, max_output_tokens=max_tokens
        )

        return response

    def summarize_file(
        self, path: str | PathLike, max_words: int = config.MAX_WORDS
    ) -> str:
        """Uses GPT model to summarize contents of given text file into
        bullet list format.

        If text content is longer than expected, file contents will be truncated.

        Raises error if given file is binary, invalid or inaccessible.

        Parameters
        ----------
        path : str | PathLike
            Path to input file to summarize into bullet list.

        max_words : int
            Maximum number of words for summary text. Default is 100 words.

        Returns
        -------
        summary : str
            File content summarized into bullet list.
        """

        try:
            with open(path, "r") as file:
                text = file.read()

            summary = self.summarize(text, max_words=max_words)
            return summary
        except Exception as ex:
            print(f"[ERROR] {ex}")
            return ""

    @validate_params([TextParam(name="review")])
    def get_sentiment(self, review: str) -> str:
        """Uses GPT model to detect sentiment in a user-supplied review.

        Parameters
        -----------
        review : str
            User-supplied review that conveys a sentiment.

        Returns
        --------
        sentiment : str
            Single-word sentiment inferred from review text : Positive, Negative, Neutral
        """

        if len(review) > config.MAX_INPUT_L:
            review = review[: config.MAX_INPUT_L]

        prompt = SENTIMENT_PROMPT.format(delimiter=self.delimiter, review=review)
        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(prompt, model=self.model, max_output_tokens=20)
        return response

    @validate_params([TextParam(name="statement")])
    def get_mental_state(self, statement: str) -> str:
        """Uses GPT model to classify mental state from a user-supplied statement.

        This feature was originally developed for a specific Kaggle dataset.

        Parameters
        -----------
        statement : str
            User-supplied statement that should normally convey a specific mental state.

        Returns
        --------
        mental_state : str
            Single-word mental state : Normal, Depression, Suicidal, Anxiety, Stress, Bi-Polar, Disorder
        """

        if len(statement) > config.MAX_INPUT_L:
            statement = statement[: config.MAX_INPUT_L]

        prompt = MENTAL_STATE_PROMPT.format(
            delimiter=self.delimiter, statement=statement
        )
        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(prompt, model=self.model, max_output_tokens=20)
        return response

    @validate_params(
        [TextParam(name="text", max_len=config.MAX_INPUT_M, fix_mode="trim")]
    )
    def translate(self, text: str, to_lang: str = "English") -> str:
        """Uses given GPT model to translate user text to a target language.

        Model is asked to automatically detect source language.

        Parameters
        -----------
        text : str
            User-supplied text that should be translated.

        to_lang : str, optional, Default = "English"
            Target language for translation.

        Returns
        --------
        translated_text : str
            User-supplied text translated into target language.
        """

        if len(text) > config.MAX_INPUT_M:
            text = clean_text(text, max_len=config.MAX_INPUT_M)

        max_output_tokens = 5000
        max_words = self._get_word_count(max_output_tokens)
        prompt = TRANSLATE_PROMPT.format(
            delimiter=self.delimiter,
            text=text,
            language=to_lang,
            max_words=max_words,
        )

        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(
            prompt, model=self.model, max_output_tokens=max_output_tokens
        )
        return response

    @validate_params(
        [TextParam(name="text", max_len=config.MAX_INPUT_M, fix_mode="trim")]
    )
    def change_tone(self, text: str, context: str = "Business") -> str:
        """Uses given GPT model to rewrite user text with a desired tone.

        Model is asked to politely refuse the request if the tone is unsupported.

        Parameters
        -----------
        text : str
            User-supplied text that should be rewritten with desired tone.

        context : str, optional, Default = "Business"
            Desired tone for transformed (i.e. rewritten) text.

        Returns
        --------
        transformed_text : str
            Text rewritten with desired tone.
        """

        if len(text) > config.MAX_INPUT_M:
            text = clean_text(text, max_len=config.MAX_INPUT_M)

        max_output_tokens = 5000
        max_words = self._get_word_count(max_output_tokens)
        prompt = REWRITE_PROMPT.format(
            delimiter=self.delimiter, text=text, context=context, max_words=max_words
        )

        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(
            prompt,
            model=self.model,
            max_output_tokens=max_output_tokens,
            temperature=0.3,
        )
        return response

    @validate_params([TextParam(name="message", max_len=config.MAX_INPUT_M)])
    def explain_error(
        self, message: str, context: str = "Unknown", max_words: int = 200
    ) -> str:
        """
        Uses GPT model to explain a user-supplied error message, with or without context.

        Parameters
        -----------
        message : str
            User-supplied error message.

        context : str, optional, Default = "Unknown"
            Optional context that guides model to give a more relevant explanation.

        max_words : int, optional, Default = 200
            Limits model explanation to a maximum count of words.

        Returns
        --------
        explanation : str
            Explanation of user-supplied error message.
        """

        if len(message) > config.MAX_INPUT_M:
            message = message[: config.MAX_INPUT_M]

        max_output_tokens = self._get_token_count(max_words)
        prompt = EXPLAIN_PROMPT.format(
            delimiter=self.delimiter,
            message=message,
            context=context,
            max_words=max_words,
        )

        if self.debug:
            print(f"Input prompt :\n{prompt}")
        response = get_completion(
            prompt, model=self.model, max_output_tokens=max_output_tokens
        )
        return response
