# 6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha",
    104: "Bhakti"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists")
    print("Name:", employees[emp_id])
else:
    print("Employee does not exist")