# Dependencies 
import csv
import os
import sys

# Files to load 
election1_csv = os.path.join("election_data_1.csv")
#election2_csv = os.path.join("election_data_2.csv")

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

print("Election Results")
print("--------------------------")
print(f"Total Votes: {Total_votes}\n"
      f"--------------------------")
    
# Find the percentage of the vote that each candidate won, print to terminal
for candidate in Candidate_votes:
    Votes = Candidate_votes.get(candidate)
    Vote_percentage = float(Votes) / float(Total_votes) * 100
    print(f"{candidate}: {Vote_percentage: .3f}% ({Votes})\n")
    
# Find the winner and output to terminal
winner = max(Candidate_votes, key=Candidate_votes.get)
print("--------------------------")
print(f"Winner: {winner}\n"
      f"--------------------------")

    
# Export the election results to the text file
#sys.stdout = open(output_file, 'w')
#print(election_results1)