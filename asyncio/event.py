import asyncio

async def waitEvent(event):
    print("Waiting for event to be set")
    await event.wait()
    print("Event Completed via Set")

async def setEvent(event):
    print("Before Event Set")
    await asyncio.sleep(2)
    event.set()
    print("After Event Set")

async def main():
    event = asyncio.Event()
    waitTask = asyncio.create_task(waitEvent(event))
    await setEvent(event)
    await waitTask

asyncio.run(main())