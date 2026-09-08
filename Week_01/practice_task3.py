# 3.Convert a temperature given in Fahrenheit (as a string input) to Celsius using type casting.
fahrenheit = str(input("Enter the temperarture: "))

fahrenheit = float(fahrenheit)
celsius = float(fahrenheit - 32) * 5/9

print("Temperature in Celsius: ", celsius)
