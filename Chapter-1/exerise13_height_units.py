"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

feet = input("Enter number of feet: ")
inches = input("Enter number of inches: ")

ft_cm = int(feet) * 30.48 
inch_cm = int(inches) * 2.54

cm = ft_cm + inch_cm

print("{}'{} inches converted to cm is {}".format(feet, inches, cm))