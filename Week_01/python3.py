# 3. Write a program to print the Fibonacci sequence up to n terms using a loop.
n=10
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b