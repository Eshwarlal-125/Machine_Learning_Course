# 10. Write a function is_palindrome(s) that returns True if a string reads the same forwards and backwards.

def is_palindrome(s):
    return s==s[::-1]

s = str(input("Enter a string: "))
print(is_palindrome(s))