import threading

event = threading.Event()

def add_product():
    print("Waiting for product addition event")
    event.wait()
    print("Event Received, Moving to Checkout")

t1 = threading.Thread(target=add_product)
t1.start()

userInput = input("Do you want to add product/. y/n")
if (userInput == 'y'):
    event.set()

# Do with Event wait and then set.
# Do with Daemon Thread