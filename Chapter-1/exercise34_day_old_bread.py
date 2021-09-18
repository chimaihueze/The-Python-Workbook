"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price.

Each of these amounts should be displayed on its own line with an appropriate label. 
All of the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.
"""

price = 3.49
discount = price * 0.6
day_old = price - discount
num_bread = int(input("Number of day old bread bread: ")) # number of day old bread 
total_price = num_bread * day_old

print("The regular price for the bread is ${:.2f}, the discount is ${:.2f}, and the total price for {} loaves is ${:.2f}".format(price, discount, num_bread, total_price))