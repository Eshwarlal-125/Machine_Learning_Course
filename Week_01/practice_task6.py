# 6.Write a program using bitwise operators to check whether a given integer is even or odd (hint: n & 1).
num = int(input("Enter a number: "))
if(num & 1):
    print("The number is odd")
else:
    print("The number is even")