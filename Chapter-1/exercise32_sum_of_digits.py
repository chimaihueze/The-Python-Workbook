"""
Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3+1+4+1=9.
"""

digits = input("Input 4 digits: ")

lst = list(digits)
b = 0

for a in lst:
    b += int(a)
print(b)
    


