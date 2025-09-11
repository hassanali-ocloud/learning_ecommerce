def f(int x) -> int:
    return x * x

def sum_of_squares(int n) -> int:
    cdef int i, total = 0
    for i in range(n):
        total += f(i)
    return total
