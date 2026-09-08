# 4. Write a function that takes a list of numbers and returns a new list with duplicates removed, preserving original order.
def remove_duplicates(numbers):
    result=[]
    for x in numbers:
        if x not in result:
            result.append(x)
    return result

print(remove_duplicates([1,2,2,3,4,3,5,1]))