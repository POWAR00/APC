class Student:
    # Constructor
    def __init__(self):
        self.roll_no = 1
        self.name = "Bhakti"
        print("Constructor called")
    # Member function
    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
    # Destructor
    def __del__(self):
        print("Destructor called")
# Creating object
s1 = Student()
# Calling member function
s1.display()