username= input("enter the username:")
if username == "admin":
    password = input("enter the password:")

    if password == "1234":
        print("Login is successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")