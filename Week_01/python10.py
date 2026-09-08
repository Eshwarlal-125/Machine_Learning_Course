# 10. Write a lambda function combined with filter() to extract all odd numbers from a list.
numbers=[1,2,3,4,5,6,7,8,9]
odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)