"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). 
In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km). 
Use your research skills to determine how to convert from MPG to L/100 km. 
Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

mpg = float(input("Enter the MPG "))
one_gallon = 3.785411784
mile2km = 1.609344

mpg_2lkm = ((100 * one_gallon) / (mile2km * mpg))
print(mpg_2lkm)
