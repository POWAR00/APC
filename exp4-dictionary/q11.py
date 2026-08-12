# 11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 92,
    "Bhakti": 85
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Marks:", students[highest_student])