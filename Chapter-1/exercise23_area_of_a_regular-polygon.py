"""
Polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. 

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""

# s is the length of a side and n is the number of sides:

import math

s = float(input("Enter the length (s): "))
n = int(input("Enter the number of sides (n): "))

area = (n * (s ** 2)) / (4 * (math.tan(math.pi / n)))

print("The area of the polygon os {:.2f}".format(area))