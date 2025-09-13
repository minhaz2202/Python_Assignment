USERNAME = "python"
PASSWORD = "rules"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    attempts += 1

    if user == USERNAME and pwd == PASSWORD:
        print("Welcome!")
        break
    else:
        print("Username or password incorrect.")

if attempts == max_attempts and (user != USERNAME or pwd != PASSWORD):
    print("Access denied.")
