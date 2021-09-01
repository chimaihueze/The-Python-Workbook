"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width 
area_in_acres = area / 43560

print("The area of the field is", area_in_acres, "acres")