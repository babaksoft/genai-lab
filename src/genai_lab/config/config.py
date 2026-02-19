from pathlib import Path

DEF_GPT_MODEL = "gpt-4o-mini"
DELIMITER = "````"
MAX_WORDS = 100
MAX_INPUT_LEN = 20_000

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = PACKAGE_ROOT / "samples"

SAMPLE_REVIEW_1 = """
This is one of the oddest movies I have watched in a long while. Usually if they are this strange
I bail out early and rarely regret it. Luckily, I held on for this one. While I can't say that this
is a great movie (it isn't), I can say that watching it is rather like a good acid trip - only a few
really awful moments and the rest filled with "did I really just see that?" wonderment. Lots of laugh
out loud moments. A great cast of characters with Meredith Eaton outstanding as the dwarf daughter-in-law
with an attitude. Keep an open mind."""

SAMPLE_REVIEW_2 = """
This was a dreadful, boring movie, even for a documentary. At times, it did provided insight to life
and also had humorous moments, but overall it was not worth seeing. Every time I began to feel
sympathetic towards Mark and began to hope he would be successful, I would become disappointed by his
lack of responsibility and drug and alcohol abuse."""
