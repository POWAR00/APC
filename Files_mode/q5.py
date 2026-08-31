file = open("demo.txt", "r+")
print(file.read())
file.write("\nNew data")
file.close()