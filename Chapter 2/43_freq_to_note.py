"""
In the previous question you converted from a note’s name to its frequency. In this
question you will write a program that reverses that process. Begin by reading a
frequency from the user. If the frequency is within one Hertz of a value listed in
the table in the previous question then report the name of the corresponding note.
Otherwise report that the frequency does not correspond to a known note. In this
exercise you only need to consider the notes listed in the table. There is no need to
consider notes from other octaves.
"""

note_freq = (("C4", 261.63), ("D4", 293.66), ("E4", 329.63), ("F4", 349.23), ("G4", 329.00), ("A4", 440.00), ("B4", 493.88))

freq = float(input("Enter the frequency (Hz): "))

for i in note_freq:
    if (i[1] - 1) <= freq <= (i[1] + 1):
        print("{} Hz has about the frequency of {}.".format(freq, i[0]))


