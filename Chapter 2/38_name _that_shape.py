"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

num_sides = int(input("Enter the number of sides: "))

# triangle = 3
# square = 4
# pentagon = 5
# hexagon = 6
# heptagon = 7
# octagon = 10
# nonagon = 9
# decagon = 10

shapes = {'triangle': 3, 'square': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8, 'nonagon': 9, 'decagon': 10}

for k, v in shapes.items():
    # print(k)
    if num_sides == v:
        print("A shape with {} sides is called {}.".format(num_sides, k))
    else:
        print("Error! Wrong input!")