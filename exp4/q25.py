#25.	Remove all duplicate elements while preserving the original order.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)