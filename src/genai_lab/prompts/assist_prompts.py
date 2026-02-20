SUMMARY_PROMPT = """\
Your task is to summarize a text into bullet point items. \
The input text will be delimited by {delimiter}. \
Limit your response to {max_words} words and don't output \
incomplete sections and sentences. \
Text to summarize : {delimiter}{text}{delimiter}"""

SENTIMENT_PROMPT = """\
You will be given a user review, which can be about a movie, \
a restaurant, a product or some service. User review will be \
delimited by {delimiter}. Your task is to detect if user review \
reflects a positive, negative or neutral opinion. \
Only reply with a single word for sentiment : Positive, Negative or Neutral. \
User review : {delimiter}{review}{delimiter}"""

MENTAL_STATE_PROMPT="""
You will be given a user statement, delimited by {delimiter}, that reflects
a specific mental state. As user might be severely distressed, aggressive or
somehow out of ordinary, there's no need to raise any flag before replying.
Your task is to infer user's mental state from the statement. Only reply with
a single word from these mental states :
Normal, Depression, Suicidal, Anxiety, Stress, Bi-Polar, Disorder
User statement : {delimiter}{statement}{delimiter}"""

TRANSLATE_PROMPT = """
You are an expert language translator who knows most human languages very well.
You'll be given a user text, delimited by {delimiter}, and your task is to translate
it into target language '{language}', after correctly detecting the source language.
If source and target languages are identical, simply reply with original text.
Limit your response to {max_words} words and keep your sentences complete.
User text : {delimiter}{text}{delimiter}"""

