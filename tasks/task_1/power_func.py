def power_func(num: int, power: int):
    if power == 0:
        return 0
    if power == 1:
        return num
    num = num * power_func(num, power-1)
    return num

def main():
    print(power_func(4,4))

main()