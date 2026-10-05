from salary import calculate_salary
from tax import calculate_tax
from bonus import calculate_bonus
basic = 30000
allowance = 5000
salary = calculate_salary(basic, allowance)
tax = calculate_tax(salary)
bonus = calculate_bonus(salary)
print("Salary:", salary)
print("Tax:", tax)
print("Bonus:", bonus)
