import threading
import time

num = 0

lock = threading.Lock()

def increment():
    global num, lock
    lock.acquire()
    for x in range(10):
        num += 1
        print("Incrementing: ", num)
    lock.release()

def decrement():
    global num, lock
    lock.acquire()
    for y in range(10):
        num -= 1
        print("Decrementing: ", num)
    lock.release()

incT = threading.Thread(target=increment)
decT = threading.Thread(target=decrement)

incT.start()
decT.start()


# Take num and double and divide
# Do with lock
# Do with Semaphore