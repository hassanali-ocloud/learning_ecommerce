import asyncio

async def modify_shared_resources(sema, resourceId):
    async with sema:
        print(f"Resource Accesssing: Id: {resourceId}")
        await asyncio.sleep(10)
        print(f"Resource Released: Id: {resourceId}")

async def main():
    sema = asyncio.Semaphore(2)
    await asyncio.gather(*(modify_shared_resources(sema, x) for x in range(5)))

asyncio.run(main())