# 18. Write a function that removes duplicate elements from a list while preserving order.
def remove_duplicates(lst):
    result=[]
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(remove_duplicates([1,2,2,3,4,3,5,1]))