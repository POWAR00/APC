# 14. Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)