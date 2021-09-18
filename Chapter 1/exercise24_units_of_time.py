"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""
secs_per_day = 60 * 60 * 24
secs_per_hour = 60 * 60
secs_per_minute = 60 


days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = (days * secs_per_day) + (hours * secs_per_hour) + (minutes * secs_per_minute) + seconds

print("The total number of seconds represented by this duration is {}".format(total_seconds))