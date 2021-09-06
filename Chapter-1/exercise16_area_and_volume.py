"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""
import math

radius = float(input("Enter the radius: ")) 

area = math.pi * (radius ** 2)
volume = (4/3) * math.pi * (radius ** 3)

print("The area of the circle is {}".format(area))
print("The volune of the sphere is {}".format(volume))