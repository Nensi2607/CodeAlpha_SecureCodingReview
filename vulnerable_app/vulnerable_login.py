username = input("Enter username: ")
password = input("Enter password: ")

stored_username = "admin"
stored_password = "admin123"

if username == stored_username and password == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password")