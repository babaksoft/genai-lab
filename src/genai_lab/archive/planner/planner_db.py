from pydantic import BaseModel, Field


class SimpleTask(BaseModel):
    id: int = Field(description="Unique identifier of task")
    title: str = Field(max_length=80, description="Short title for task")
    priority: int = Field(ge=1, le=5, description="Priority of task (1: highest priority, 5: lowest priority)")
    duration: float = Field(gt=0.0, le=8.0, description="Estimated completion time for task")
    deadline: str = Field(description="Due date for task")

# Note: Some durations are unrealistically prolonged to simulate a busy full week
TASKS = [
    SimpleTask(
        id=1,
        title="Visit barbershop to get a haircut",
        priority=3,
        duration=2.0,
        deadline="2026-05-31"
    ),
    SimpleTask(
        id=2,
        title="Read chapter 7 of MLOps book by [...]",
        priority=2,
        duration=6.0,
        deadline="2026-05-27"
    ),
    SimpleTask(
        id=3,
        title="Implement simple monitoring for project X",
        priority=1,
        duration=4.0,
        deadline="2026-05-28"
    ),
    SimpleTask(
        id=4,
        title="Add unit tests for data pipeline in project Y",
        priority=2,
        duration=5.0,
        deadline="2026-05-26"
    ),
    SimpleTask(
        id=5,
        title="Meet Emma in coffeeshop",
        priority=1,
        duration=3.0,
        deadline="2026-05-25T16:00"
    ),
    SimpleTask(
        id=6,
        title="Work on new post about Agentic AI in your blog",
        priority=3,
        duration=6.0,
        deadline="2026-05-30"
    ),
    SimpleTask(
        id=7,
        title="Review PR #4567 in XYZ repo",
        priority=1,
        duration=4.5,
        deadline="2026-05-26"
    ),
    SimpleTask(
        id=8,
        title="Order newly released psychology book before discount offer is due (for Emma)",
        priority=1,
        duration=1.5,
        deadline="2026-05-31"
    ),
    SimpleTask(
        id=9,
        title="Read chapter 9 of MLOps book by [...]",
        priority=2,
        duration=4.0,
        deadline="2026-05-28"
    ),
    SimpleTask(
        id=10,
        title="Review PR #1234 in ABC repo",
        priority=2,
        duration=4.0,
        deadline="2026-05-31"
    ),
]
