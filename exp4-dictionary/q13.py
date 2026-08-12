# 13. Create a dictionary containing student names and marks. Calculate the average marks of all students.

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 92,
    "Bhakti": 85
}

total = sum(students.values())
average = total / len(students)

print("Average marks:", average)