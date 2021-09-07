"""
Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).

Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2. You can use the formula vf =  vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known
"""
import math 

h = float(input("Enter the height(in meters): "))
i_speed = 0
acc = 9.8

vf = math.sqrt((i_speed ** 2) + (2 * acc * h))

print("It will hit the ground at {:.2f}m/s".format(vf))