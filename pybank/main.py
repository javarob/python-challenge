import os
import csv

budget_csv = os.path.join("./Resources", "budget_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file
    for row in csv_reader:
        print(row)
        # if current row = user input
        # if float(row[7]) >= 5:
        #     if row == 1:
        #         print(f"Cereal: {header[0]} Fiber: {header[7]}")
        #     print(f"Cereal: {row[0]} Fiber: {row[7]}")
        #     found = True
        # else keep searching
    # if nothing found print not found
# if (found == False):
#     print("No Cereals found")

