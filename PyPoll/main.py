import os
import csv

election_csv=os.path.join("C:\\Users\\18312\\Documents\\PythonStuff\\Python_Challenge\\PyPoll\\election_data.csv")

print()
print("Election Results")
print("----------------------")

canidates={}
total_votes=0

with open(election_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    for row in csvreader:

        total_votes=total_votes+1
        canidate = row[2]

        if canidate in canidates:
          canidates[canidate] = canidates[canidate] + 1
        else:
          canidates[canidate] = 1   
        
print("Total Votes: " + str(total_votes))
print("---------------------------")


for canidate, num in canidates.items():
    percent=round(int(num)/total_votes*100,2)
    print(canidate + ": " + str(percent) + "% " + "("+ str(num) + ")")
    
print("---------------------------")
#print("Winner: " + str(winner))
print("---------------------------")
print()