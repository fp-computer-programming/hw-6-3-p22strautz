# Author: SCT (AMDG) 11/15/21

lst = []

lst = [int(numbers) for numbers in input("Enter a list of 5 numbers seperated by spaces:\n").split()]

lst2 = lst.copy()

lst2.sort()

if lst2 == lst:
    print("The list is sorted")
else:
    print("The list is not sorted")
