#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

# Import modules
import os
import csv

# Set path for CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
TotalNumberVotes = 0
CandidatesWithVotes = {}

with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row

    # Calculate the total number of votes and votes for each candidate
    for row in csv_reader:
        TotalNumberVotes += 1
        current_candidate = row[2]

        # Increment the vote count for the current candidate
        if current_candidate in CandidatesWithVotes:
            CandidatesWithVotes[current_candidate] += 1
        else:
            CandidatesWithVotes[current_candidate] = 1

# Print the election results
print("Election Results")
print("---------------------------------------------------------------------")

# Print the total number of votes
print(f"Total Votes: {TotalNumberVotes}")
print("---------------------------------------------------------------------")

# Initialize variables to keep track of the winning candidate and their votes
winning_candidate = ""
winning_votes = 0

# Calculate and print the percentage of votes for each candidate
for candidate, votes in CandidatesWithVotes.items():
    percentage = (votes / TotalNumberVotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Check if the current candidate has more votes than the current winner
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

# Print the winner
print("---------------------------------------------------------------------")
print(f"Winner: {winning_candidate}")
print("---------------------------------------------------------------------")

# Write the results to a text file in the Analysis folder
output_path = os.path.join("Analysis", "election_results.txt")

# Open the file in write mode
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------------------------------------------\n")
    file.write(f"Total Votes: {TotalNumberVotes}\n")
    file.write("---------------------------------------------------------------------\n")

    # Loop through each candidate and their votes to write their details to the file
    for candidate, votes in CandidatesWithVotes.items():
        percentage = (votes / TotalNumberVotes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    file.write("---------------------------------------------------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write("---------------------------------------------------------------------\n")

# File will be automatically closed after the 'with' block