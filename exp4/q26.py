"""26.	Store marks of 20 students in a list and determine:
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Number of students scoring above average 
•	Number of students scoring below average
"""
marks = []

for i in range(20):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / 20

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above)
print("Students below average:", below)
