def is_it_single(num: int):
    counter = 0
    while num > 0:
        num = num // 10
        counter += 1
    if counter > 1:
        return False
    else:
        return True

def sum_digits(num, sum):
    if is_it_single(num):
        return sum
    
    sum = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum += rem
    
    return sum_digits(sum, sum)

def main():
    print(sum_digits(25267, 0))

main()