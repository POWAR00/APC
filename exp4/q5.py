"""5.	Create a list of student names. Remove:
•	First student 
•	Last student 
•	A specific student by name 
Display the remaining list.
"""
list=["ram","sham","om","seeta","geeta"]
list.pop(0)
list.pop()
list.remove("om")
print(list)