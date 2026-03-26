from pathlib import Path

DEF_GPT_MODEL = "gpt-4o-mini"
DELIMITER = "````"
MAX_WORDS = 100
MAX_INPUT_L = 20000
MAX_INPUT_M = 2000

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = PACKAGE_ROOT / "samples"
