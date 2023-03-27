import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = float(input("Enter score: "))
    message = get_result(score)
    print(message)
    generate_random_score()


def generate_random_score():
    """Generate random score and print the result of that score."""
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    score = random_score
    print(get_result(score))


def get_result(score):
    """Determine the result of the score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()
