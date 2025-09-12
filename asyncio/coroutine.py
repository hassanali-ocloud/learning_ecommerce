import asyncio

async def fetch_data(delay):
    print("Going to fetch data")
    await asyncio.sleep(delay)
    print("Data Fetched")
    num = delay**2
    return {"data": num, "status": "pass" if delay % 2 == 0 else "fail"}

async def acknowledge_data_via_future(future, delay):
    print("Going to fetch data")
    await asyncio.sleep(delay)
    num = delay**2
    future.set_result({"data": num, "status": "pass" if delay % 2 == 0 else "fail"})
    print("Data Fetched")

# async def main():
#     '''Waiting for single task'''
#     task = fetch_data(2)
#     result = await task
#     print(f"Result Received: {result}")

# async def main():
#     '''Waiting for multiple tasks'''
#     task1 = fetch_data(2)
#     task2 = fetch_data(3)
#     result1 = await task1
#     result2 = await task2
#     print(f"Results Received: \n Result1: {result1} & Result2: {result2}")

# async def main():
#     '''Waiting for multiple tasks via asyncio.createtasks'''
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(fetch_data(2))
#     task3 = asyncio.create_task(fetch_data(3))
    
#     result1 = await task1
#     result2 = await task2
#     result3 = await task3
    
#     print(f"Results Received: \n Result1: {result1} & Result2: {result2} & Result3: {result3}")

# async def main():
#     '''Waiting for multiple tasks via asyncio.gather'''
#     allTasks = asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
#     result = await allTasks
    
#     print(f"Results Received: \n Result: {result}")

# async def main():
#     '''Usuage of asyncio.TaskGroup'''
#     tasks = []
#     async with asyncio.TaskGroup() as tg:
#         for i, sleep_time in enumerate([1,2,3]):
#             task = tg.create_task(fetch_data(sleep_time))
#             tasks.append(task)
    
#     for task in tasks:
#         result = task.result()
#         if (result["status"] == "pass"):
#             print(f"Task with data: {result["data"]} passed")
#         else:
#             print(f"Task with data: {result["data"]} failed")

async def main():
    '''Waiting task via future'''
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    asyncio.create_task(acknowledge_data_via_future(future, 2))

    result = await future
    print(f"Result Received: {result}")

asyncio.run(main())