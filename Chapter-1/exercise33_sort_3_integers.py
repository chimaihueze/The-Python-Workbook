"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

integers = int(input("Enter 3 integers: "))

# convert int to str 
integ = str(integers)
lst = list(integ)
# print(lst)
a = '0'
lst.sort(key = int)
# print(lst)
for i in lst:
    i = str(i)
    a += i
srt = a[1:]
print("The sorted form of the {} is {}".format(integers, int(srt)))

    
    