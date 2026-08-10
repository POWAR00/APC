"""28.	Store scores of a batsman in 10 matches and calculate:
•	Highest score 
•	Lowest score 
•	Total runs 
•	Average runs 
•	Number of centuries (≥100) 
•	Number of half-centuries (50–99)
"""
scores = []

for i in range(10):
    score = int(input("Enter score: "))
    scores.append(score)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / 10

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)