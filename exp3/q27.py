email=input("Enter email address:")

if "@" in email and "." in email:
    at=email.index("@")
    dot=email.rfind(".")

    if at>0 and dot>at+1 and dot<len(email)-1:
        print("Valid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")