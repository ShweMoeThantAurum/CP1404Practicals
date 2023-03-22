def main():
    score = float(input("Enter score: "))
    message = get_result(score)
    print(message)


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
