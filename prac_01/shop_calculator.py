SENTINEL = 0
THRESHOLD_PRICE = 100  # $100
DISCOUNT_RATE = 0.10  # 10%
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < SENTINEL:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > THRESHOLD_PRICE:
    total_price = total_price - (total_price * DISCOUNT_RATE)
    print(f"Total price for {number_of_items} items is $ {total_price:,.2f}")
else:
    print(f"Total price for {number_of_items} items is $ {total_price:,.2f}")
