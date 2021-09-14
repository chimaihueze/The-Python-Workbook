"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the Internet.
"""

temp_cels = int(input("Enter temp (Celcius): "))

temp_fahr = (temp_cels * 9/5) + 32
temp_kelv = temp_cels + 273.15
print("{} degrees Celsius equates to {} degrees Fahrenheit and {}K respectively".format(temp_cels, temp_fahr, temp_kelv))