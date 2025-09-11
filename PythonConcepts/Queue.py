import queue
import random

numLs = ["Hello-5", "Hello-10", "Hello-15", "Hello-20", "Hello-25", ]

fifoQueue = queue.Queue()
for x in numLs:
    fifoQueue.put(x)
while not fifoQueue.empty():
    print(fifoQueue.get())

print("=======================================")

lifoQueue = queue.LifoQueue()
for x in numLs:
    lifoQueue.put(x)
while not lifoQueue.empty():
    print(lifoQueue.get())

print("=======================================")

pQueue = queue.PriorityQueue()
for x in numLs:
    pQueue.put((random.randint(1, 100), f"num: {x}"))
while not pQueue.empty():
    print(pQueue.get())