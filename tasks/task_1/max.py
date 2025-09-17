def find_2_max(a, b, c):
    if a > b and a > c:
        if b > c:
            return a, b
        else:
            return a, c
    elif b > c and b > a:
        if c > a:
            return b, c
        else:
            return b, a
    elif c > a and c > b:
        if a > b:
            return c, a
        else:
            return c, b

def main():
    print(find_2_max(a=7, b=1, c=4))

main()