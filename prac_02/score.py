def main():
    import random
    score = float(input("Enter score: "))
    message = get_result(score)
    print(message)
    random_score = random.randint(0, 100)
    score = random_score
    print(get_result(score))


def get_result(score):
    if score < 0 or score > 100:
        message = "Invalid score"
    elif score >= 90:
        message = "Excellent"
    elif score >= 50:
        message = "Passable"
    else:
        message = "Bad"
    return message


main()
