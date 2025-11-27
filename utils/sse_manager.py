from fastapi import Request
from fastapi.responses import StreamingResponse
import asyncio
from typing import AsyncGenerator

async def sse_event_generator(task_func, *args, **kwargs) -> AsyncGenerator[str, None]:
    """
    Async generator that yields progress updates from the background task.
    """
    queue = asyncio.Queue()

    async def run_task():
        try:
            async for progress in task_func(*args, **kwargs):
                await queue.put(progress)
        finally:
            await queue.put(None)

    asyncio.create_task(run_task())

    while True:
        event = await queue.get()
        if event is None:
            break
        yield f"data: {event}\n\n"

async def sse_response(task_func, *args, **kwargs):
    return StreamingResponse(sse_event_generator(task_func, *args, **kwargs), media_type="text/event-stream")
