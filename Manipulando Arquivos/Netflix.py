import csv


arquivo = list()
with open("advertising.csv", "r") as file:
    arquivo = csv.DictReader(file)


    for date in arquivo:
        print(date)