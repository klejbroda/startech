complete = False
user = {"admin": "12345", "moni": "67890", "domi": "67890", "jaca": "67890", "iga": "67890", "piotr": "67890"}

while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        print(f"Password is not valid for {username}. ")
        continue
    elif password == user[username]:
        print(f"Welcome {username} ")
        print(f"Thank you for logging on. ")
        complete = True

print("Username and Password Validated")