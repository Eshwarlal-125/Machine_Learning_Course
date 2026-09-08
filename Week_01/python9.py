# 9. Write a program that checks whether a given string is a palindrome, ignoring case and spaces.
s="Madam"
s=s.replace(" ","").lower()
print(s==s[::-1])