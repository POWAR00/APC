"""13.	Accept 10 numbers and sort them in:
•	Ascending order 
•	Descending order
"""
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Ascending order:", sorted(numbers))
print("Descending order:", sorted(numbers, reverse=True))