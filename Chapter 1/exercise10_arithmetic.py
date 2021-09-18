"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b • The difference when b is subtracted from a • The product of a and b • The quotient when a is divided by b • The remainder when a is divided by b • The result of log10 a • The result of ab
"""

a = int(input("Enter integer a: "))
b = int(input("Enter integrer b: "))

addition = a + b 
sub = a - b     
mult = a * b  
div = a / b  
remainder = a % b 

import math
log = math.log10(a)

print(addition)
print(sub)
print(mult)
print(div)
print(remainder)
print(log) 