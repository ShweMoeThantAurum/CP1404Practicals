MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score) # No problem with potential undefinable variable
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def show_stars(score):
    for i in range(score):
        print("*", end="")
    print()


def print_result(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    print(message)


def get_valid_score():
    score = int(input("Score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
