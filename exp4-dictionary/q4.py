# 4. Create a dictionary containing student marks. Update the marks of a specified student.

marks = {
    "Amit": 75,
    "Rahul": 80,
    "Sneha": 90,
    "Bhakti": 85
}

name = input("Enter student name: ")

if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")