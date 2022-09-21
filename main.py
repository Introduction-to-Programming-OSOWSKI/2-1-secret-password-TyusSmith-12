def password(p):
    if p == "Knights19":
        return("ACCESS GRANTED")
    elif p != "Knights19":
        return("ACCESS DENIED")

print(password("Knights19"))
