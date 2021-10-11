"""
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
                    Note    Frequency (Hz)
                    C4      261.63
                    D4      293.66
                    E4      329.63
                    F4      349.23
                    G4      392.00
                    A4      440.00
                    B4      493.88

Begin by writing a program that reads the name of a note from the user and displays the note’s frequency. 
Your program should support all of the notes listed previously.

Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8. 
While this could be done by adding many additional cases to your if statement, such a solution is
cumbersome, inelegant and unacceptable for the purposes of this exercise. 
Instead, you should exploit the relationship between notes in adjacent octaves. 
In particular, the frequency of any note in octave n is half the frequency of the corresponding note in octave n + 1. 
By using this relationship, you should be able to add support for the additional notes without adding additional cases to your if
statement.

"""

# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392.00
# A4 = 440.00
# B4 = 493.88

note_freq = (("C4", 261.63), ("D4", 293.66), ("E4", 329.63), ("F4", 349.23), ("G4", 329.00), ("A4", 440.00), ("B4", 493.88))

name = input("Enter name of note: ")

# print(note)
# print(octave)

try:
    
    for i in note_freq:
   
        
        if letter == i[0][0]:
            letter = name[0]
            octave = int(name[1])
            freq = i[1]
            freq2 = freq/(2**(4-octave))
    
    print("The frequency of note {} is {:.2f} Hz".format(name, freq2))
    
except:
        print("Error! There's no such note as '{}', please try again!".format(name))
    

    


