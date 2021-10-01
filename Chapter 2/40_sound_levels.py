"""
Write a program that reads a sound level in decibels from the user. 
If the user enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise.

If the user enters a number of decibels between the noises listed then your program should display a message
indicating which noises the value is between. 
Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, 
and for a value larger than the loudest noise in the table.
"""

decibels = int(input("Enter the Decibel level: "))
sounds = [["Jackhammer", 130], ["Gas Lawnmover", 106], ["Alarm Clock", 70], ["Quiet Room", 40]]
noise = {"Jackhammer": 130, "Gas Lawnmower": 106, "Alarm Clock": 70, "Quiet Room": 40}
lst = []

for key, value in noise.items():
    
    if not value in lst:
        lst.append(value)

min_lst = min(lst)
max_lst = max(lst)

if decibels < min_lst:
    print("{} dB is less than Quiet Room".format(decibels))

elif decibels > max_lst:
    print("{} dB is greater than Jackhammer".format(decibels))

else:
    for key, value in noise.items():
        
        if decibels == value:
            print("{} is equal to {} dB".format(key, value))  


    for s in range(len(sounds)):
        if sounds[s][1] > decibels and decibels > sounds[s+1][1]:
            print("{} dB is between {} and {}". format(decibels, sounds[s][0], sounds[s+1][0]))
           
    
    
    
    

    