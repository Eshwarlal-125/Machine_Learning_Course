# 7. Write a dictionary comprehension to create a dictionary mapping each character in a string to its frequency.
s="hello"
freq={x:s.count(x) for x in s}
print(freq)