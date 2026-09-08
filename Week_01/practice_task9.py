# 9. Write a function factorial(n) that returns n! using a while loop.
def factorial(n):
    result=1
    while n>0:
        result*=n
        n-=1
    return result

n = int(input("Enter a number: "))
print(factorial(n))