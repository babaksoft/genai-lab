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
