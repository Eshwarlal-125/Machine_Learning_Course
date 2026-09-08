# 11. Write a function stats(*nums) that returns a tuple of (min, max, average) using *args.
def stats(*nums):
    return (min(nums),max(nums),sum(nums)/len(nums))

print(stats(10,20,30,40,50))