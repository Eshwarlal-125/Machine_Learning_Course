# 5. Write a program that counts the number of vowels, consonants, digits, and spaces in a given string.
s="Hello World 123"
vowels=consonants=digits=spaces=0
for x in s:
    if x.lower() in "aeiou":
        vowels+=1
    elif x.isalpha():
        consonants+=1
    elif x.isdigit():
        digits+=1
    elif x==" ":
        spaces+=1
print(vowels,consonants,digits,spaces)