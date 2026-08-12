# 9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "Java": "James Gosling"
}

for key, value in languages.items():
    print(key, ":", value)