MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    import random
    score = float(input("Enter score: "))
    message = get_result(score)
    print(message)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    score = random_score
    print(get_result(score))


def get_result(score):
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
