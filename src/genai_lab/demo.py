import argparse
import asyncio
import logging

from workflows import Context, Workflow, step
from workflows.events import Event, StartEvent, StopEvent

from genai_lab.config.logging import configure_logging

logger = logging.getLogger(__name__)


class StreamEvent(Event):
    sequence: int


class GreetingFlow(Workflow):
    @step
    async def greet(self, ctx: Context, ev: StartEvent) -> StopEvent:
        for i in range(3):
            ctx.write_event_to_stream(StreamEvent(sequence=i+1))
            await asyncio.sleep(0.5)

        name = ev.get("name", "World")
        if not name:
            name = "stranger"
        return StopEvent(result=f"Hello, {name}!")


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="Who am I supposed to greet?",
        type=str,
        default=""
    )

    return parser.parse_args()


async def main() -> None:
    args = get_args()

    wf = GreetingFlow(workflow_name="Greeting", timeout=30, verbose=True)
    handler = wf.run(name=args.name)
    logger.info("Workflow '%s' started.", wf.workflow_name)

    async for event in handler.stream_events(expose_internal=True):
        if isinstance(event, StreamEvent):
            logger.info("StreamEvent: sequence=%d", event.sequence)
        else:
            logger.info("Event: type=%s", type(event).__name__)

    result = await handler
    logger.info("Workflow '%s' completed: result=%s", wf.workflow_name, result)


if __name__ == "__main__":
    configure_logging()
    asyncio.run(main())
