def double_each_index(array: list[int]):
    return list(map(lambda x: x * x, array))

def main():
    print(double_each_index([1,2,3,4,5]))

main()