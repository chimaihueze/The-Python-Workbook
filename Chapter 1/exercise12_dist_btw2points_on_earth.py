"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. 

The distance between these points, following the surface of the Earth, in
kilometers is: distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

The value 6371.01 in the previous equation wasn’t selected at random. It is the
average radius of the Earth in kilometers.

Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.

Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians.
"""

import math

lat1 = float(input("Enter the latitude 1: "))
long1 = float(input("Enter the longitude 1: "))
lat2 = float(input("Enter the latitude 2: "))
long2 = float(input("Enter the longitude 2: "))

dist = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1-long2))
print(dist)