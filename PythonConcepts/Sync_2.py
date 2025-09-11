import threading
import time

num = 0

semaphore = threading.BoundedSemaphore(value=2)

def access_to_resource(thread_num):
    global num, semaphore
    print(f"Thread: {thread_num}: Trying to Access to num ")
    semaphore.acquire()
    print(f"Thread: {thread_num}: Giving Access to num ")
    time.sleep(5)
    print(f"Thread: {thread_num}: Releasing Access to num ")
    semaphore.release()

for x in range(10):
    t = threading.Thread(target=access_to_resource, args=(x,))
    t.start()
    time.sleep(1)