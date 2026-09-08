# 20. Create a tuple of (name, marks) pairs and sort the list of tuples by marks in descending order.
students=[("Ali",85),("Ahmed",92),("Sara",78),("John",95)]
students.sort(key=lambda x:x[1],reverse=True)
print(students)