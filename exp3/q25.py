text=input("Enter a string:")
frequency={}

for ch in text:
    frequency[ch]=frequency.get(ch,0)+1

first=max(frequency.values())
second=0

for ch in frequency:
    if frequency[ch]<first and frequency[ch]>second:
        second=frequency[ch]
        character=ch

print("Second most frequent character:",character)
print("Frequency:",second)