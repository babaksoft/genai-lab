"""
Initialize environment variables from .env file
"""


def init():
    from dotenv import find_dotenv, load_dotenv

    _ = load_dotenv(find_dotenv())
