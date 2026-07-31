# ruff: noqa: F403, F405

__all__ = [
    "VALUE_ERROR",
    "TRUNC_MESSAGE",
    "TRIM_MESSAGE",
]

VALUE_ERROR = """
The value of '{param_name}' cannot be None, empty or
 a whitespace-only string."""
TRUNC_MESSAGE = """
[WARN] This feature accepts maximum length of {max_len}
 for '{param_name}', but a string with length {param_len}
 was given. Long strings will be truncated."""
TRIM_MESSAGE = """
[WARN] This feature accepts maximum length of {max_len}
 for '{param_name}', but a string with length {param_len}
 was given.

Long texts will be truncated to the longest complete text
 shorter than {max_len} characters."""
