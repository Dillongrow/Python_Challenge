import os
import csv

budget_csv=os.path.join("C:\\Users\\18312\\Documents\\PythonStuff\\Python_Challenge\\PyBank\\budget_data.csv")

print()
print("Financial Analysis")
print("-------------------------------")

total_months=0
total_sum=0
previous=0
change=0
total_change=0
avg_change=0
greatest_inc=0
greatest_dec=9999999

with open(budget_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    for row in csvreader:

        total_months=total_months+1
        total_sum=total_sum + int(row[1])
        
        change=int(row[1])-previous
        previous=int(row[1])
        total_change=total_change+change

        if change > greatest_inc:
            greatest_inc=change
        if change < greatest_dec:
            greatest_dec=change

    avg_change=total_change/total_months     

print("Total Months: " + str(total_months))
print("Total: $" +str(total_sum))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " +  " $" +str(greatest_inc))
print("Greatest Decrease in Profits: $" +str(greatest_dec))
print()