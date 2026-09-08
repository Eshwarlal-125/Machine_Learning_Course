# 6. Write a function multiply(*args) that returns the product of any number of arguments using *args.
def multiply(*args):
    result=1
    for x in args:
        result*=x
    return result

print(multiply(2,3,4))