from datetime import datetime
from itertools import filterfalse

from genai_lab.planner.planner_db import TASKS


def all_tasks() -> list[dict]:
    """
    Return all tasks in database

    Returns:
        list[dict]: List of all tasks in database
    """
    return [t.model_dump() for t in TASKS]


def task_by_id(task_id: int) -> dict:
    """
    Return a single task by unique identifier

    Args:
        task_id (int): Unique identifier of task to return

    Returns:
        dict: Task information as a simple dictionary
    """
    ids = [t.id for t in TASKS]
    if task_id not in ids:
        raise ValueError(f"No task with id {task_id} could be found.")
    by_id = next(filterfalse(lambda t: t.id != task_id, TASKS))
    return by_id.model_dump()


def tasks_by_priority(priority: int) -> list[dict]:
    """
    Return all tasks having specified priority

    Args:
        priority (int): Priority of tasks to return (1: highest priority, 5: lowest priority)

    Returns:
        list[dict]: A list of all tasks having specified priority
    """
    if priority not in range(1, 6):
        raise ValueError("Invalid priority (must be an integer between 1 and 5)")

    return [t.model_dump() for t in filterfalse(lambda x: x.priority != priority, TASKS)]


def tasks_by_deadline(deadline: str) -> list[dict]:
    """
    Return all tasks having specified deadline

    Args:
        deadline (str): Required due date for task (ISO format)

    Returns:
        list[dict]: A list of all tasks having specified deadline
    """
    try:
        date = datetime.fromisoformat(deadline).date()
        return [t.model_dump()
                for t in filterfalse(lambda x: datetime.fromisoformat(x.deadline).date() != date, TASKS)]
    except Exception:
        raise ValueError("Invalid date format (must be valid ISO format)")
