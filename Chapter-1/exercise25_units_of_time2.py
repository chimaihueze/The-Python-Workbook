"""
Develop a program that begins by reading a number of seconds from the user. 
Then your program should display the equivalent amount of time in the form D:HH:MM:SS, where D,
HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that they occupy exactly two digits.

Use your research skills determine what additional character needs to be included in
the format specifier so that leading zeros are used instead of leading spaces when a
number is formatted to a particular width.
"""

secs_per_day = 60 * 60 * 24
secs_per_hour = 60 * 60
secs_per_minute = 60 

seconds = int(input("Enter number of seconds: "))

days = int(seconds / secs_per_day)

hours = int((seconds % secs_per_day) / secs_per_hour)

minutes = int(((seconds % secs_per_day) % secs_per_hour) / secs_per_minute)

secs = (((seconds % secs_per_day) % secs_per_hour) % secs_per_minute)

print("{} seconds contain {:02d}:{:02d}:{:02d}:{:02d}".format(seconds, days, hours, minutes, secs))