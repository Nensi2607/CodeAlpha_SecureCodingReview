import hashlib

stored_username = "admin"

stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and entered_password_hash == stored_password_hash:
    print("Secure login successful!")
else:
    print("Invalid username or password")