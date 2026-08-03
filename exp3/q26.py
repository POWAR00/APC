text=input("Enter a message:")
key=int(input("Enter key:"))
encrypted=""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted+=chr((ord(ch)-ord('A')+key)%26+ord('A'))
        else:
            encrypted+=chr((ord(ch)-ord('a')+key)%26+ord('a'))
    else:
        encrypted+=ch

print("Encrypted message:",encrypted)

decrypted=""

for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted+=chr((ord(ch)-ord('A')-key)%26+ord('A'))
        else:
            decrypted+=chr((ord(ch)-ord('a')-key)%26+ord('a'))
    else:
        decrypted+=ch

print("Decrypted message:",decrypted)