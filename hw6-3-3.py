# Author: SCT (AMDG) 11/15/21

lst = []

lst = [int(numbers) for numbers in input("Enter a list of 5 numbers seperated by spaces:\n").split()]

total = int(lst[0]) + int(lst[1]) + int(lst[2]) + int(lst[3]) + int(lst[4])

print(total)
