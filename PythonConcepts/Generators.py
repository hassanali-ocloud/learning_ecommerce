def customGen(x):
    while True:
        print(f"Doing expo for: {x}")
        yield x**3
    
    # for x in range(n):
    #     print(f"Doing expo for: {x}")
    #     yield x**3

values = customGen(10)

# Running the iterator behind the scene
# for x in values:
#     print(x)
print(next(values))
print(next(values))