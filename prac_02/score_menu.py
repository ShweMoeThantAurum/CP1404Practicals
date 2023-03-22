MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        score = int(input("Score: "))
        while score < 0 or score > 100:
            print("Invalid score")
            score = int(input("Score: "))
    elif choice == "P":
        if score < 0 or score > 100:
            message = "Invalid score"
        elif score >= 90:
            message = "Excellent"
        elif score >= 50:
            message = "Passable"
        else:
            message = "Bad"
        print(message)
    elif choice == "S":
        for i in range(score):
            print("*" * i)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Farewell")

