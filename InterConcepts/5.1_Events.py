import threading
import time

def worker():
    time.sleep(5)
    print("Worker finished!")

# t = threading.Thread(target=worker)
t = threading.Thread(target=worker, daemon=True)
t.start()
print("Main program exiting...")
