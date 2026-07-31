# Lessons learned

## Planner (agent demo)

Sample output from Planner experiment shows some notable LLM behavior I should pay attention to.

- Due to **knowledge cut-off**, LLMs do NOT have an accurate perception of current date.
- Using relative dates (today, tomorrow, etc.) in LLM prompts will result in **naive bugs**.
- One simple solution is to start a prompt with current date, as I did in my 3rd and 4th runs.
- Needless to say, this kind of date specification needs a **prompt template**.

## Assistant (LLM capabilities demo)

When I asked ChatGPT to review my prompts (as a **Senior ML/AI engineer**), I got great feedback
I need to use in my future prompts. Here's a summary of prompting techniques I learned.

- **Explicit output contract:** Control LLM response generation (e.g. Do not include ..., Only answer with X or Y, etc.)
- The above technique is particularly important if LLM response will be consumed by code.
- **"Use only the given input" guard:** Control LLM creativity or background knowledge injection
- The above technique is especially useful for:
  - Summarization
  - Classification
  - Troubleshooting
- **Minimal fallback rule:** Improve robustness of prompts by clear hints (e.g. If you are not certain, reply with: "Unknown")
- The above technique is extremely valuable for:
  - Mental health classification
  - Sentiment detection
  - Translation edge cases
- **Clarification:** In a typical sentiment classification scenario where Neutral is an option, help LLM (e.g. Use "Neutral" only if no clear positive or negative sentiment is expressed.)
- **LLM social bias:** In "rewrite" prompt, I explicitly asked GPT model to reject invalid contexts and explain the reason. Interestingly, when I tried an invalid context (i.e. Flirtatious) GPT behavior was inconsistent: sometimes it rejected, but most often it didn't! Explicit instructions should help, although I haven't tried it yet.

