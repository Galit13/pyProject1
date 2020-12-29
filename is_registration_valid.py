username = input("enter your email address:")

if "@" in username and "." in username:
    password = input("enter your password:")
    if "#" in password and len(password) >= 8:
        print("valid username and password")
    else:
        print("invalid password")
else:
    print("invalid username")