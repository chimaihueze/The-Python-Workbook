"""
Write a program that implements the Anonymous Gregorian Computus algorithm
to compute the date of Easter. Your program should read the year from the user and
then display a appropriate message that includes the date of Easter in that year.
"""

from math import floor
import calendar

year = int(input("Enter year: "))

a = year % 19 
b = floor(year / 100)
c = year % 100
d = floor(b / 4)
e = int(b % 4)
f = floor((b + 8) / 25)
g = floor((b - f + 1) / 3)
h = ((19 * a) + int(b) - int(d) - int(g) + 15) % 30
i = floor(c / 4)
k = c % 4
l = (32 + (2 * e) + (2 * int(i)) - h - k) % 7
m = floor((a + (11 * h) + (22 * l)) / 451)
month = int(floor(h + l - (7 * m) + 114) / 31)
day = 1 + (((h + l - (7 * int(m)) + 114) % 31))
mn = calendar.month_name[month]

print("In {}, Easter fell on {} {}". format(year, mn, day))