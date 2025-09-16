def find_2_max(a, b, c):
    values = [a, b, c]
    values.sort(reverse=True)
    return values[0], values[1]

def main():
    print(find_2_max(a=4, b=2, c=8))

main()