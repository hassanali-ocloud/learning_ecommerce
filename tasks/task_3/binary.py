def binary(num: int):
    val: int = 0
    i = 1
    while num > 0:
        rem = num % 2
        num = int(num / 2)
        val = val + (rem * i)
        i *= 10
    return val

def main():
    print(binary(10.00))

main()