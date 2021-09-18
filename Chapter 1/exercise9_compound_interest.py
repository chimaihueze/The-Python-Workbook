"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
"""

amnt_deposited = float(input("Enter amount deposited: "))
year1 = amnt_deposited + (amnt_deposited * 0.04)
year2 = year1 + (year1 * 0.4)
year3 = year2 + (year2 * 0.4)

print(("The amount in the savings account after the first, second and third year are {:.2f}, {:.2f}, and {:.2f} respectively").format(year1, year2, year3))