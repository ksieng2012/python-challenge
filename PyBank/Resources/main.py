#PyBank

#Import Required packages
import os
import csv

# * In this challenge, you are tasked with creating a Python script for analyzing the financial 
# records of your company. You will give a set of financial data called [budget_data.csv]
# (PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Read CSV files
csvpath = os.path.join("Resources", "budget_data.csv")
# print(csvpath)

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first. and remove it from the data
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)

# Store Data in a list
    data = list(csvreader)
    unzip_data=list(zip(*data))
    profit_cols=[int(x) for x in unzip_data[1]]
    month_list=unzip_data[0]

    # for row in data:
    #     print(row)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

    #   The total number of months included in the dataset
    month = len(data)
    print(f"Total months : {month}")

    #   * The net total amount of "Profit/Losses" over the entire period
    # profit_cols=unzip_data[1]
    profit= sum(profit_cols)
    print(f"Net Profits : ${profit}")
        
    #   * The average of the changes in "Profit/Losses" over the entire period
        # change month to month list
    change_m2m=[profit_cols[i+1]-profit_cols[i] for i in range(len(profit_cols)-1)]
    avg_change=sum(change_m2m)/len(change_m2m)
    avg_changef="{:.2f}".format(avg_change)
    print(f"Average Change ${avg_changef}")
    
#   * The greatest increase in profits (date and amount) over the entire period
        # find max change index 
    max_i=[i for i in range(len(change_m2m)) if change_m2m[i] == max(change_m2m)]
    max_i=int(max_i[0])
    max_month=str(month_list[int(max_i) +1])
    print(f"Greatest increase in profit: {max_month} (${change_m2m[max_i]})")
    

#   * The greatest decrease in losses (date and amount) over the entire period
    min_i=[i for i in range(len(change_m2m)) if change_m2m[i] == min(change_m2m)]
    min_i=int(min_i[0])
    min_month = month_list[int(min_i) +1]
    print(f"Greatest decrease in profit: {min_month} (${change_m2m[min_i]})")


# # * As an example, your analysis should look similar to the one below
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_path = os.path.join("Result.txt")

with open(output_path, 'w', newline='') as f:
    f.write('Financial Analysis\n'
            '----------------------------\n')
    f.write(f'Total Months: {month}\n')
    f.write(f'Total Profits: {profit}\n')
    f.write(f'Average  Change: ${avg_changef}\n')
    f.write(f'Greatest Increase in Profits: {max_month} (${change_m2m[max_i]})\n')
    f.write(f'Greatest Decrease in Profits: {min_month} (${change_m2m[min_i]})\n')



