#23.	Count the frequency of each element in a list.
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of each element:")

for num in frequency:
    print(num, ":", frequency[num])