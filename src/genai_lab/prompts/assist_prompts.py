SUMMARY_PROMPT = """\
Your task is to summarize a text into bullet point items. \
The input text will be delimited by {delimiter}. \
Limit your response to {max_words} words and don't output \
incomplete sections and sentences. \
Text to summarize : {delimiter}{text}{delimiter}"""
