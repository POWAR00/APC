"""29.	Store the temperature of 30 days and determine:
•	Hottest day 
•	Coldest day 
•	Average temperature 
•	Days above average temperature 
•	Days below average temperature
"""
temperatures = []

for i in range(30):
    temp = float(input("Enter temperature: "))
    temperatures.append(temp)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / 30

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest day temperature:", hottest)
print("Coldest day temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)