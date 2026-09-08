# 14. Given a list of numbers, use list comprehension to create a new list containing only the squares of even numbers.
numbers=[1,2,3,4,5,6,7,8]
squares=[x**2 for x in numbers if x%2==0]
print(squares)