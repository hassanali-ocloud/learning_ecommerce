def squareANum(fun, para):
    return fun(para)

print("Square: ", squareANum(lambda x : x*x, 5))

def SortTupleList(tupleList):
    return sorted(tupleList, key=lambda x: x[1])

print("Sort: ", SortTupleList([(2, 'b'), (1, 'a'), (3, 'c')]))
