# Eddie King
# September 23, 2026
# P2LAB1 - Circle Calculations
# This program calculates the diameter, circumference, and area of a circle using a radius entered by the user.

# Pseudocode:
# 1. Ask the user to enter the radius of a circle.
# 3. Calculate the diameter.
# 4. Calculate the circumference.
# 5. Calculate the area.
# 6. Display the results with the required decimal formatting.

#Import math module to use the constant, math.pi
import math

#Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

#Display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate area
area = math.pi * radius**2

#Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}")