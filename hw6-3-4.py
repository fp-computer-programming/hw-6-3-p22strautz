# Author: SCT (AMDG) 11/15/21

lst = input("Input any list of numbers or letters seperated by spaces.\n")

ask = str.lower(input("Do you want to find the middle or the end?\n"))

lst2 = lst.split()
length = len(lst2)

if ask == "middle":
    print(lst2[1:length - 1])
elif ask == "end":
    print(lst2[:1] + lst2[length - 1:])
