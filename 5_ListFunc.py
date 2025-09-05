from functools import reduce

numLs = [5, 2, 1, 4, 6]

sqrNumLs = list(map(lambda x: x*x, numLs))
print("Sqr Num: ", sqrNumLs)

evenNumLs = list(filter(lambda x: x%2==0, numLs))
print("Even Num: ", evenNumLs)

prod = reduce(lambda x,y: x*y, numLs, 1)
print("Prodct of All Elements: ", prod)

maxVal = reduce(lambda acc, i: max(acc, i), numLs, numLs[0])
print(f"Max Val: {maxVal}")
