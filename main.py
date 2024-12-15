username_valid = False

while not username_valid:
    username = input("Username: ")
    username = username.strip()

    if not username:
        print("Please enter a username")

    else:
        username_valid = True

password_valid = False

while not password_valid:
    password = input("Password: ")

    if not password:
        print("Please enter a password")

    else:
        password_valid = True
