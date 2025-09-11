import threading

def func1():
    for x in range(10):
        print("Exec Thread-1")

def func2():
    for x in range(10):
        print("Exec Thread-2")

def func3():
    for x in range(10):
        print("Exce Thread-3")

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)
thread3 = threading.Thread(target=func3)

thread3.start()
thread2.start()
thread3.join()
print("Wait Complete")
thread1.start()

# General thread code
# Run two threads
# 