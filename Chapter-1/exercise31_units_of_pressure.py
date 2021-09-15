"""
In this exercise you will create a program that reads a pressure from the user in kilopascals.
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

kpa = float(input("Enter the pressure (KP): "))

psi = kpa / 6.89475729
mmhg = kpa * 7.50062

print("{}kpa is equivaloent to {:.2f}psi and {:.2f}mmhg".format(kpa, psi, mmhg))