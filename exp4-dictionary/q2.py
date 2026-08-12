# 2. Create a dictionary containing employee information and display the value associated with a specified key.

employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 45000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")