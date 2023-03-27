MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = 0
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == 0:
                score = get_valid_score()
            elif score is not None:
                print_result(score)
        elif choice == "S":
            if score == 0:
                score = get_valid_score()
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def show_stars(score):
    """Print as many stars as the score."""
    for i in range(score):
        print("*", end="")
    print()


def print_result(score):
    """Determine the result of the score."""
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
    """Check whether the score input is valid or not."""
    valid_input = False
    while not valid_input:
        try:
            score = int(input("Score: "))
            valid_input = True
        except ValueError:
            print("Not a valid integer")
    return score  # No problem with potential undefinable variable


main()
