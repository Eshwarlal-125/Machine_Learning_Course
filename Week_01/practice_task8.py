# 8.Print all prime numbers between 1 and 100 using nested loops and break.
for i in range(2,101):
    isPrime = True
    for j in range(2,i):
        if(i%j==0):
            isPrime = False
            break
    if(isPrime):
        print(i, end=" ")