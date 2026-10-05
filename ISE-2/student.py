import numpy as np
students = np.array(["Amit", "Priya", "Rahul", "Sneha", "Vikas"])
marks = np.array([75, 88, 62, 95, 70])
average = marks.mean()
print("Average marks:", average)
above_average = students[marks > average]
print("Students scoring above average:")
print(above_average)
