# 17. Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common_keys = set(dict1.keys()) & set(dict2.keys())

print("Common keys:", common_keys)