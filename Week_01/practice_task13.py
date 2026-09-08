# 13. Using a lambda function with map(), convert a list of Celsius temperatures to Fahrenheit.
celsius=[0,10,20,30,40]
fahrenheit=list(map(lambda c:(c*9/5)+32,celsius))
print(fahrenheit)