"""27.	Store salaries of employees and determine:
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning above ₹50,000 
•	Employees earning below ₹30,000 
"""
salaries = []

for i in range(10):
    salary = int(input("Enter salary: "))
    salaries.append(salary)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)