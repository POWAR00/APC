"""30.	Store patient names and ages using lists.
Perform:
•	Add a patient 
•	Delete a patient 
•	Search a patient 
•	Display all patients 
•	Count total patients
"""
names = ["Amit", "Bhakti", "Rahul"]
ages = [25, 20, 30]

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
names.append(name)
ages.append(age)

delete = input("Enter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)

search = input("Enter patient name to search: ")

if search in names:
    index = names.index(search)
    print("Patient found:", names[index], ages[index])
else:
    print("Patient not found")

print("All patients:")

for i in range(len(names)):
    print(names[i], ages[i])

print("Total patients:", len(names))