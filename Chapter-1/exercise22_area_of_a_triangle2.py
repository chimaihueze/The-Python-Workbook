"""
Compute the area of a triangle when the lengths of all three sides are known. 
Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2. 
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.
"""
import math 

s1 = float(input("Enter s1: "))
s2 = float(input("Enter s2: "))
s3 = float(input("Enter s3: "))

s = (s1 + s2 + s3)/2

area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("The area of the triangle is {:.2f}".format(area))
