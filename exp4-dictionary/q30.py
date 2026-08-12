# 30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

students = {
    "Bhakti": "CSE",
    "Rahul": "IT",
    "Amit": "CSE",
    "Sneha": "ENTC",
    "Priya": "IT"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)

print(groups)