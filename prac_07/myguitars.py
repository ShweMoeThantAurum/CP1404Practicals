from prac_06.guitar import Guitar

FILENAME = "guitars.csv"
guitars = []
with open(FILENAME, "r") as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    print(guitars)
    guitars.sort()
    print(guitars)

name = input("Name: ").title()
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = name, year, cost
    guitars.append(guitar_to_add)
    print(guitars)
    print(f"{guitar_to_add}, added.")
    name = input("Name: ").title()
with open(FILENAME, "w") as out_file:
    for guitar in guitars:
        out_file.write(str(guitar) + "\n")

