"""7.	Accept 10 numbers from the user and store them in a list. Calculate:
•	Sum 
•	Average 
"""
list=[]
for i in range(10):
    num=int(input("Enter numbers:"))
    list.append(num)
total=sum(list)
average=total/10
print("list",list)
print("Total",total)
print("Average",average)