#14.	Create a list containing duplicate values and display only unique elements.
numbers = [10, 20, 10, 30, 20, 40, 30, 50, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)