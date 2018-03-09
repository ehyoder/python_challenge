# Dependencies 
import csv
import os
import sys

# Files to load 
election1_csv = os.path.join("election_data_1.csv")
election2_csv = os.path.join("election_data_2.csv")

# Output file
output_file = "new_election_data.txt" 

# Lists and dictionaries to store data 
Candidates = []
Candidate_votes = {}
Percentage_won = []
Total_votes = []
Total_votes = 0 

# Open the first file and read as a dictionary
with open(election1_csv, 'r') as csvfile:
    csvreader= csv.DictReader(csvfile, delimiter= ',')

    # Iterate over each row to find data
    for row in csvreader:
        Total_votes = Total_votes + 1

        # Assign candidate_name as key
        Candidate_name = row["Candidate"]
        # If a candidate's name is not in the list of candidates, add it to that list
        if Candidate_name not in Candidates: 
            Candidates.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0

        # Track the votes for each candidate
        Candidate_votes[Candidate_name] = Candidate_votes[Candidate_name] + 1

Election_results1 = (
    f"Election Results\n" 
    f"--------------------------\n"
    f"Total Votes: {Total_votes}\n"
    f"--------------------------")
print(Election_results1)
    
# Find the percentage of the vote that each candidate won, print to terminal
for candidate in Candidate_votes:
    Votes = Candidate_votes.get(candidate)
    Vote_percentage = float(Votes) / float(Total_votes) * 100
    Vote_data1 = (f"{candidate}: {Vote_percentage: .1f}% ({Votes})\n")
    print(Vote_data1)
    
# Find the winner and output to terminal
winner = max(Candidate_votes, key=Candidate_votes.get)
Winning_candidate1 = (
      f"--------------------------\n"
      f"Winner: {winner}\n"
      f"--------------------------\n")
print(Winning_candidate1)

################################################# SECOND FILE #####################################################

# Open the second file and read as a dictionary
with open(election2_csv, 'r') as csvfile:
    csvreader= csv.DictReader(csvfile, delimiter= ',')

    # Iterate over each row to find data
    for row in csvreader:
        Total_votes = Total_votes + 1

        # Assign candidate_name as key
        Candidate_name = row["Candidate"]
        # If a candidate's name is not in the list of candidates, add it to that list
        if Candidate_name not in Candidates: 
            Candidates.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0

        # Track the votes for each candidate
        Candidate_votes[Candidate_name] = Candidate_votes[Candidate_name] + 1

Election_results2 = (
    f"Election Results2\n" 
    f"--------------------------\n"
    f"Total Votes: {Total_votes}\n"
    f"--------------------------")
print(Election_results2)
    
# Find the percentage of the vote that each candidate won, print to terminal
for candidate in Candidate_votes:
    Votes = Candidate_votes.get(candidate)
    Vote_percentage = float(Votes) / float(Total_votes) * 100
    Vote_data2 = (f"{candidate}: {Vote_percentage: .1f}% ({Votes})\n")
    print(Vote_data2)
    
# Find the winner and output to terminal
winner = max(Candidate_votes, key=Candidate_votes.get)
Winning_candidate2 = (
      f"--------------------------\n"
      f"Winner: {winner}\n"
      f"--------------------------\n")
print(Winning_candidate2)

# Export the election results to the text file
sys.stdout = open("new_election_data.txt", 'w')
print(f" {Election_results1}\n {Candidate_votes}\n {Winning_candidate1}\n {Election_results2}\n {Vote_data2}\n {Winning_candidate2}")