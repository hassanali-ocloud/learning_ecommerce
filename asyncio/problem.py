import asyncio

async def delay_task(name, delay):
    print(f"Execution Start of task name: {name}")
    await asyncio.sleep(delay)
    print(f"Execution Complete of task name: {name}")

def parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None

async def main():
    allTasks = []
    
    while True:
        num_of_tasks = input("Please enter the number of tasks (1-Inifinity): ")
        if parse_int(num_of_tasks) == None or int(num_of_tasks) <= 0:
            print("Error: Invalid Value")
            continue
        else:
            break

    i=0
    while i<int(num_of_tasks):
        while True:
            task_name = input("Please enter the name of task: ")
            if task_name == "":
                print("Error: Invalid Task Name: ")
                continue
            else:
                break

        while True:
            task_delay = input("Please enter the delay you want to add for this task (Range: 1-Infinite): ")
            if (parse_int(task_delay) == None or int(task_delay) <= 0):
                print("Error: Invalid Value")
                continue
            else:
                break
        allTasks.append(delay_task(task_name, int(task_delay)))
        i += 1

    for task in allTasks:
        await task
    
asyncio.run(main())