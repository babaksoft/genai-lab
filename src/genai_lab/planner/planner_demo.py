import asyncio

from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import FunctionAgent

from genai_lab.planner.planner_tools import (
    all_tasks,
    task_by_id,
    tasks_by_priority,
    tasks_by_deadline,
)

load_dotenv()

GPT_MODEL = "gpt-4o-mini"
SYS_PROMPT = """
You are an assistant capable of providing task information and planning services using tools.
"""
llm = OpenAI(model=GPT_MODEL)
agent = FunctionAgent(
    llm=llm,
    tools=[all_tasks, task_by_id, tasks_by_priority, tasks_by_deadline],
    system_prompt=SYS_PROMPT,
)


async def simple_task():
    message = "Today is 25 May 2026. What are my lowest-priority tasks for the next 7 days?"
    print("[User]:\n", message)
    response = await agent.run(user_msg=message)
    print("[GPT]:\n", response)


if __name__ == "__main__":
    asyncio.run(simple_task())
