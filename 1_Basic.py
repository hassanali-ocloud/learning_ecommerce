def NumEvenOdd():
    num = int(input("Enter Number: "))
    if (num%2==0):
        print("Its an Even")
    else:
        print("Its an Odd")

def CountVowels():
    vowelsStr = input("Enter the string: ")
    count = 0
    for i in vowelsStr:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count+=1
    print(f"Number of Vowels: {count}")

CountVowels()