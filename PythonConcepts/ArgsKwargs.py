def demo(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

demo(1, 2, 3, a="10", b=20)