import os
import csv

candidate = "" 
exists = False
vote_total = 0
candidate_vote_count = 0
votes_by_candidate ={}
prior = 0
winner = ""

budget_csv = os.path.join("./Resources", "election_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    # loop through file by line
    for row in csv_reader:  # grab each line in csv
        vote_total = vote_total + 1 # get total number of records
        
        candidate = row[2] # grab candidate by name
        for x in range(len(votes_by_candidate)):  # for each candidate (key) in dict 
            if candidate in votes_by_candidate:   # if candidate is listed in dict
                exists = True
                votes_by_candidate[candidate] = votes_by_candidate[candidate] + 1 # add to vote cnt
                break
            else:
                exists = False # key not already in dict

        if exists == False:  # key wasn't in dict so add & add vote cnt too
            votes_by_candidate[candidate] = 1

print("  ")
print("Election Results")
print("------------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------------")
for key,val in votes_by_candidate.items(): # list candidates and votes
    if val > prior: # find highest votes
        prior = val
        winner = key
    print (f"{key}:  {round(val/vote_total*100, 3)}% ({val}) ")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")
