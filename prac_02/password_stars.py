MINIMUM_PASSWORD_LENGTH = 8
password = input("Enter your password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    password = input("Enter your password: ")
for i in range(len(password)):
    print("*", end=" ")
