# ruff: noqa: F403, F405

import inspect
from dataclasses import dataclass
from functools import wraps
from typing import Callable

from ..config import config
from ..config.messages import *


def clean_text(text: str, max_len: int) -> str:
    """Shortens a possibly long input text, up to the last complete sentence.

    If the text length does not exceed given maximum length, original text is returned.
    """

    if len(text) <= max_len:
        return text

    trunc_text = text[:max_len]
    idx_stop = trunc_text.rfind(".")
    idx_qm = trunc_text.rfind("?")
    idx_excl = trunc_text.rfind("!")
    idx_max = sorted([idx_stop, idx_qm, idx_excl], reverse=True)[0]

    return trunc_text[: idx_max + 1]


@dataclass
class TextParam:
    name: str
    required: bool = True
    max_len: int = config.MAX_INPUT_L
    fix_mode: str | None = None


def _check_param(param: TextParam, value: str | None) -> None:
    if param.required and not value:
        message = VALUE_ERROR.format(param_name=param.name)
        raise ValueError(message)

    value = value.strip() if value else ""
    if len(value) > param.max_len:
        message = TRUNC_MESSAGE if not param.fix_mode else TRIM_MESSAGE
        message = message.format(
            max_len=param.max_len, param_name=param.name, param_len=len(value)
        )
        print(message)


def validate_params(params: list[TextParam]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper_validate_params(*args, **kwargs):
            bound = inspect.signature(func).bind(*args, **kwargs)
            bound.apply_defaults()

            for param in params:
                value = bound.arguments.get(param.name)
                _check_param(param, value)

            return func(*args, **kwargs)

        return wrapper_validate_params

    return decorator
