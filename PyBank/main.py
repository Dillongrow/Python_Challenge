import os
import csv

budget_csv=os.path.join("C:\\Users\\18312\\Documents\\PythonStuff\\Python_Challenge\\PyBank\\budget_data.csv")

print("Financial Analysis")
print("-------------------------------")

total_months=0
total_sum=0
with open(budget_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)



    for row in csvreader:

        total_months=total_months+1
        total_sum=total_sum + int(row[1])

        
print("Total Months: " + str(total_months))
print("Total: $" +str(total_sum))