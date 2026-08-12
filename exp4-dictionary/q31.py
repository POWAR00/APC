# 32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target: "))

data = {}

for num in numbers:
    required = target - num

    if required in data:
        print("Numbers:", required, num)
        break

    data[num] = True
else:
    print("No pair found")