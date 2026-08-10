"""Create a list of numbers. Add:
One element at the end 
One element at the beginning 
One element at a specified position 
Display the updated list.
"""
list=[10,20,30,40]
print("Element is inserted at end is",list.append(50))
print("Element inserted at beginning",list.insert(0,5))
print("Element inserted at position",list.insert(2,25))
print(list)