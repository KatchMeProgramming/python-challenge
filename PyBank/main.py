#PyBank Instructions
#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
#You will be given a financial dataset called budget_data.csv. 
#The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import modules
import os
import csv

# Set path for CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
TotalMonths = 0
NetTotalProfitLosses = 0
ProfitLossesList = []
GreatestProfitIncreasesAmount = 0
GreatestProfitIncreasesDate = ""
GreatestProfitDecreasesAmount = 0
GreatestProfitDecreasesDate = ""

with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row

    previous_profit_loss = 0 # Initalize previous profit / lost value
    
    for row in csv_reader:

        #Calculate Total Months and Net Total Profit Losses
        TotalMonths += 1
        NetTotalProfitLosses += int(row[1])
        
        # Calculate profit/loss change
        current_profit_loss = int(row[1])
        if TotalMonths > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            ProfitLossesList.append(profit_loss_change)

             # Calculate the Greatest Increase in Profits and corresponding date
            if profit_loss_change > GreatestProfitIncreasesAmount:
                GreatestProfitIncreasesAmount = profit_loss_change
                GreatestProfitIncreasesDate = row[0] 

             # Calculate the Greatest Decrease in Profits and corresponding date
            if profit_loss_change < GreatestProfitDecreasesAmount:
                GreatestProfitDecreasesAmount = profit_loss_change
                GreatestProfitDecreasesDate= row[0] 
        
        previous_profit_loss = current_profit_loss

        # Calculate the Average Profit Losses Changes
        if len(ProfitLossesList) > 0:
            AverageProfitLossesChanges = sum(ProfitLossesList) / len(ProfitLossesList)

        else:
            AverageProfitLossesChanges = 0

print("Financial Analysis")
print("---------------------------------------------------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetTotalProfitLosses}")
print(f"Average Change: ${AverageProfitLossesChanges:.2f}")
print(f"Greatest Increase in Profits: {GreatestProfitIncreasesDate}, $({GreatestProfitIncreasesAmount})")
print(f"Greatest Decrease in Profits: {GreatestProfitDecreasesDate}, $({GreatestProfitDecreasesAmount})")

# Write the results to a text file in the Analysis folder
output_path = os.path.join("Analysis", "budget_data_analysis.txt")

file = open(output_path, "w")

file.write("Financial Analysis \n")
file.write("--------------------------------------------------------------------- \n")
file.write(f"Total Months: {TotalMonths} \n")
file.write(f"Total: ${NetTotalProfitLosses} \n")        
file.write(f"Average Change: ${AverageProfitLossesChanges:.2f} \n")
file.write(f"Greatest Increase in Profits: {GreatestProfitIncreasesDate}, $({GreatestProfitIncreasesAmount}) \n")
file.write(f"Greatest Decrease in Profits: {GreatestProfitDecreasesDate}, $({GreatestProfitDecreasesAmount}) \n")

# Close the file
file.close()