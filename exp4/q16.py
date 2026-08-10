"""16.	Create a nested list storing:
•	Student Name 
•	Roll Number 
•	Marks 
Display all student details
"""
students = [
    ["Bhakti", 101, 85],
    ["Amit", 102, 78],
    ["Rahul", 103, 90],
    ["Sneha", 104, 88]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
