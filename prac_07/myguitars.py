import csv

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
