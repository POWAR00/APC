"""6.	Write a program to find the largest and smallest number in a list without using max() or min()."""
list=[10,20,90,23,17,3,30,40,50]
list.sort()
print("Smallest number is",list[0])
print("Largest number is",list[-1])