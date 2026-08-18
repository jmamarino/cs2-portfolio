import math

x1 = float(input("Enter your x1: "))
y1 = float(input("Enter your y1: "))
x2 = float(input("Enter your x2: "))
y2 = float(input("Enter your y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"The distance between the two points is: {distance:.2f}")

#Reflection:
#Using the math library is more practical because it gives the functions like sqrt() and pow().
#Instead of writing long calculations from the start to calculate square roots, We can accomplish the task in a single line of code.
#It saves time, keeps the code looking good and clean, and prevents the calculation errors using the math library.


