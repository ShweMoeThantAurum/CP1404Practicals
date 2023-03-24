def main():
    MINIMUM_PASSWORD_LENGTH = 8
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        password = get_password()
    for i in range(len(password)):
        print("*", end=" ")


def get_password():
    """Get the password from the user."""
    password = input("Enter your password: ")
    return password


main()
