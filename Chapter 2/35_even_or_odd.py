"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))