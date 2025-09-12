import asyncio

shared_resources = 0
lock = asyncio.Lock()

async def modify_shared_resources():
    global shared_resources
    async with lock:
        print(f"Resource before modification: {shared_resources}")
        shared_resources += 1
        await asyncio.sleep(1)
        print(f"Resources after modification: {shared_resources}")

async def main():
    await asyncio.gather(*(modify_shared_resources() for _ in range(5)))

asyncio.run(main())