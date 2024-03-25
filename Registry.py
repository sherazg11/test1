username = input("Enter Your Username: ")
pass1 = input("Enter Password: ")

if username[::-1] in pass1 or username in pass1:
    print("Username Cant Be In Password")
else:
    pass2 = input("Confirm Password: ")
    if len(pass1) < 8:
        print("Weak Password.")
    elif len(pass1) >= 8:
        print("Srong Password.")
        if pass1==pass2:
            print("Account Created.")
        else:
            print("Password Doesnt Match.")
    else:
        print("Something Went Wrong.")