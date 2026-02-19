from pathlib import Path

DEF_GPT_MODEL = "gpt-4o-mini"
DELIMITER = "````"
MAX_WORDS = 100
MAX_CHARS_IN = 20_000

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = PACKAGE_ROOT / "samples"
