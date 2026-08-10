"""9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list."""
list=["Kolhapur","Satara","Sangali","Pune","Mumbai","Delhi","Panhala","Bhuyewadi"]
city=input("enter you city").title()
if city in list:
        print("City is present")
else:
    print("not present")