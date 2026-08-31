try:
    file = open("newfile.txt", "x")
    file.write("New file created")
    file.close()
    print("File created successfully")
except FileExistsError:
    print("File already exists")