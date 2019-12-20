import os
import csv

election_csv=os.path.join("C:\\Users\\18312\\Documents\\PythonStuff\\Python_Challenge\\PyPoll\\election_data.csv")

print()
print("Election Results")
print("----------------------")

canidates={}

with open(election_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    for row in csvreader:

      canidate = row[2]

      if canidate in canidates:
        canidates[canidate] = canidates[canidate] + 1
      else:
        canidates[canidate] = 1 
        
print("Total Votes:")
print("-----------------")
for canidate, num in canidates.items():
    print(canidate + ": " + str(num))
