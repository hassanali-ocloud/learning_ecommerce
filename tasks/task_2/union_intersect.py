def union(arr1: list[int], arr2: list[int]):
    set_arr = set(arr1)
    for x in arr2:
        set_arr.add(x)
    return set_arr

def intersection(arr1: list[int], arr2: list[int]):
    set_arr = set(arr1)    
    new_arr = []
    for x in arr2:
        if set_arr.__contains__(x):
            new_arr.append(x)
    return new_arr

def main():
    arr1 = [7, 1, 5, 2, 3, 6]
    arr2 = [3, 8, 6, 20, 7]
    print(union(arr1, arr2))
    print(intersection(arr1, arr2))

main()