file = open("demo.bin", "ab")
file.write(b" More data")
file.close()
print("Binary data appended")