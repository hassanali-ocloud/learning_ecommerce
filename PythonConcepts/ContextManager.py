from contextlib import contextmanager

class Animal:
    def __enter__(self):
        print("Logging: Entering Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Logging: Exiting Contenxt")
        print(exc_type)

with Animal() as animal:
    print("Working on animal resource")

@contextmanager
def Tiger_Context():
    print("Entering")
    yield "resource"
    print("Exiting")

with Tiger_Context() as r:
    print("Using", r)
