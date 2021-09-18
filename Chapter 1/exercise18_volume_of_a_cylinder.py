"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal
"""
import math 

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))

volume = math.pi * (r **2 ) * h

print("The volume of the cycliner is {:.1f}".format(volume))
