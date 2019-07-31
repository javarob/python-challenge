import os
import csv

count_rows = 0
sum_rows = 0
previous_profit = 0
previous_date = 0
current_profit = 0
current_date = 0
average_change = 0
least_profit = 100000000
least_profit_date = ""
highest_profit = 0
highest_profit_date = ""
profit_difference = 0

budget_csv = os.path.join("./Resources", "budget_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file by line
    for row in csv_reader:
        count_rows = count_rows + 1 # get total number of records
        # print(row)
        sum_rows = sum_rows + int(row[1]) # sum total of all profits
        current_profit = int(row[1]) 
        current_date = row[0]
        
        if count_rows > 1: # for first row where previous is empty
           profit_difference = (current_profit - previous_profit)
           if profit_difference > highest_profit: # track highest profit
               highest_profit = profit_difference
               highest_profit_date = current_date
           if profit_difference < least_profit: # track least profit
               least_profit = profit_difference
               least_profit_date = current_date

           average_change = average_change +  profit_difference # add profit changes - average @ report
           previous_profit = current_profit
           previous_date = current_date
        else: # set previous for next difference calculation
           previous_profit = current_profit
           previous_date = current_date
           

print("  ")
print("Finacial Analysis")
print("------------------------------")
print(f"Total Months: {count_rows}")
print(f"Total: ${sum_rows}")
average_change = average_change / (count_rows -1) #calc average change
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatist Increase in Profits: {highest_profit_date}  (${highest_profit})")
print(f"Greatist Decrease in Profits: {least_profit_date}  (${least_profit})")
