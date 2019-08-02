import os
import csv

vcount = 0
candidate = "" 
candidates = []
exists = False
vote_total = 0
candidate_vote_count = 0
votes_by_candidate ={}
total_val = 0 # temp for tsting

budget_csv = os.path.join("./Resources", "election_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file by line
    for row in csv_reader:
        vote_total = vote_total + 1 # get total number of records
        
        candidate = row[2]
        for x in range(len(candidates)):
            if candidate == candidates[x]:
                exists = True
                vcount = vcount + 1
                votes_by_candidate[candidate] = votes_by_candidate[candidate] + 1
                #print(f"votes: {votes_by_candidate[candidate]}")
                break
            else:
                exists = False

        if exists == False:
            candidates.append(candidate)
            vcount = vcount + 1
            votes_by_candidate[candidate] = 1

    # for candidate in candidates:
    #     print(candidate)

for key,val in votes_by_candidate.items():
    total_val = total_val + val
    print (key," => ",val)


# print("  ")
# print(find_candidates)
print(f"row count: {vote_total}")
print(f"votes total {total_val}")
        

           

# 
# print("Finacial Analysis")
# print("------------------------------")
# print(f"Total Months: {count_rows}")
# print(f"Total: ${sum_rows}")
# average_change = average_change / (count_rows -1) #calc average change
# print(f"Average Change: ${round(average_change, 2)}")
# print(f"Greatist Increase in Profits: {highest_profit_date}  (${highest_profit})")
# print(f"Greatist Decrease in Profits: {least_profit_date}  (${least_profit})")
