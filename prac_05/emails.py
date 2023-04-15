def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = get_full_name_from_email(email)
        confirmation = input(f"Is your name {full_name}? (Y/n) ").upper()
        if confirmation == "N" and confirmation != "":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_full_name_from_email(email):
    """Extract full name from email address"""
    prefix = email.split("@")[0]
    name_parts = "".join(prefix).split(".")
    full_name = " ".join(name_parts).title()
    return full_name


main()