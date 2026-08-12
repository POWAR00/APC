# 12. Create a dictionary containing student names and marks. Find the student with the lowest marks.

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 92,
    "Bhakti": 65
}

lowest_student = min(students, key=students.get)

print("Student with lowest marks:", lowest_student)
print("Marks:", students[lowest_student])