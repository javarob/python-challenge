import os
import csv

count_rows = 0
sum_rows = 0
previous_profit
previous_date
current_profit
current_date
average_change = 0
greatest_increase = 0
greatest_decrease = 0

budget_csv = os.path.join("./Resources", "budget_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file
    for row in csv_reader:
        count_rows = count_rows + 1
        sum_rows = sum_rows + int(row[1])
        current_profit = int(row[1])
        current_date = row[0]
        if count_rows > 1:
           average_change = average_change + (current_profit - previous_profit)
           previous_profit = current_profit
           previous_date = current_date
        else:
           previous_profit = current_profit
           previous_date = current_date
            

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {count_rows}")
print(f"Total: ${sum_rows}")
average_change = average_change / total_months
print(f"Average Change: ${average_change}")

  