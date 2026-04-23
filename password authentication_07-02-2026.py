# Password Authentication Program

correct_password = "Secure@123"

attempts = 3

while attempts > 0:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Wrong password! Attempts left:", attempts)

if attempts == 0:
    print("Account Locked. Too many wrong attempts.")