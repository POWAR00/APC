# 33. Take a string, use a dictionary to find the first character that occurs only once.

text = input("Enter string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character")