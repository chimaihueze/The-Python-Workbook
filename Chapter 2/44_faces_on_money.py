"""
                    Individual          Amount
                    George Washington     $1
                    Thomas Jefferson      $2
                    Abraham Lincoln       $5
                    Alexander Hamilton    $10
                    Andrew Jackson        $20
                    Ulysses S. Grant      $50
                    Benjamin Franklin     $100
                    
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.
"""

amount = int(input("Enter the denomination: "))
notes = [1, 2, 5, 10, 20, 50, 100]

individual = {"George Washington": 1,
              "Thomas Jefferson": 2,
              "Abraham Lincoln": 5,
              "Alexander Hamilton": 10,
              "Andrew Jackson": 20,
              "Ulysses S. Grant": 50,
              "Benjamin Franklin": 100}

if amount in notes:
    for k, v in individual.items():
        if amount == v:
            print("The face of {} is printed on ${} note.".format(k, v))
else:
    print("This note does not exist! Please try again.")
        
        
        
