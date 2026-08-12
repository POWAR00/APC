# 25. Create a dictionary containing student names and marks. Develop a program to add a student, update marks, delete a student, search for a student, display all students, find the highest marks, and calculate the average.

students = {
    "Amit": 75,
    "Rahul": 88,
    "Sneha": 92
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print("Highest:", name, students[name])

    elif choice == 7:
        if students:
            print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")