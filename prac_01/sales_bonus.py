"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SENTINEL = 0
SALES_THRESHOLD = 1000
LOW_BONUS_RATE = 0.10  # 10%
HIGH_BONUS_RATE = 0.15  # 15%
sales = float(input("Enter sales: $"))
while sales >= SENTINEL:
    if sales < SALES_THRESHOLD:
        bonus = int(sales * LOW_BONUS_RATE)
    else:
        bonus = int(sales * HIGH_BONUS_RATE)
    print(bonus)
    sales = float(input("Enter sales: $"))
