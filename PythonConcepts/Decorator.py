def customDecorator(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print("Custom Decoration Done. Now returning")
        return val
    return wrapper

@customDecorator
def callWithDeco(animal):
    print(f"Animal is: {animal}")
    return f"Returning Animal: {animal}"

print(callWithDeco("Parrot"))    