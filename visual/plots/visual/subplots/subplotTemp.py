import matplotlib.pyplot as plt
import csv
with open("temps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    headings = next(csv_reader)
    for values in csv_reader:
        print(values)