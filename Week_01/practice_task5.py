# 5.Given radius r, compute and print the area and circumference of a circle (use round() to 2 decimals).
r = float(input("Enter the Radius: "))

pi = 3.14
area = float(pi*(r*r))
circumference = float(2*pi*r)

print("Area of Circle: ", area)
print("Circumference of Circle: ", circumference)

