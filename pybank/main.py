import os
import csv

count_rows = 0
sum_rows = 0
previous_profit = 0
previous_date = 0
current_profit = 0
current_date = 0
average_change = 0
least_profit = 0
least_profit_date = ""
highest_profit = 0
highest_profit_date = ""

budget_csv = os.path.join("./Resources", "budget_data_test.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file
    for row in csv_reader:
        count_rows = count_rows + 1
        # print(row)
        sum_rows = sum_rows + int(row[1])
        current_profit = int(row[1])
        current_date = row[0]
        if current_profit > highest_profit:
            highest_profit = current_profit
            highest_profit_date = current_date
        if current_profit < least_profit:
            least_profit = current_profit
            least_profit_date = current_date
        if count_rows > 1:
           average_change = average_change + (current_profit - previous_profit)
           previous_profit = current_profit
           previous_date = current_date
        else:
           previous_profit = current_profit
           previous_date = current_date



print("  ")
print("Finacial Analysis")
print("------------------------------")
print(f"Total Monthss: {count_rows}")
print(f"Total: ${sum_rows}")
average_change = average_change / (count_rows -1)
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatist Increase in Profits: {highest_profit_date}  (${highest_profit})")
print(f"Greatist Decrease in Profits: {least_profit_date}  (${least_profit})")

  