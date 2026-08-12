# 20. Create a dictionary and display its elements in ascending order of keys.

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

for key in sorted(data):
    print(key, ":", data[key])