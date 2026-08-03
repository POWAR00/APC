text1=input("Enter first string:")
text2=input("Enter second string:")
if sorted(text1)==sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")