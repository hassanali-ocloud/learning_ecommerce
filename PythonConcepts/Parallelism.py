from multiprocessing import Pool

def generateFactoral(x):
    if x <= 1:
        return 1
    else:
        val = x * generateFactoral(x-1)
        print("Val: ", val)
        return val

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(generateFactoral, [1, 2, 3, 4]))
