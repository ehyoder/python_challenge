# Dependencies 
import csv
import os
import sys

# Files to load 
election1_csv = os.path.join("election_data_1.csv")
#election2_csv = os.path.join("election_data_2.csv")

# Output file
#output_file = new_election_data.txt 

# Lists and dictionaries to store data 
Total_votes = []
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
    
        # Skip header row    
        #next(csvreader)
  
        # Store the election results as a variable and print the winning candidate (to terminal)
    election_results1 = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {Total_votes}\n"
        f"--------------------\n"
        #f"{Candidate}: {Percentage_won} ({Candidate_votes})\n"
        #f"{Candidate}: {Percentage_won} ({Candidate_votes})\n"
        #f"{Candidate}: {Percentage_won} ({Candidate_votes})\n"
        #f"{Candidate}: {Percentage_won} ({Candidate_votes})\n"
        #f"Winner: {Winning_Candidate})"
        f"--------------------\n")
    print(election_results1)

# Export the election results to the text file
#sys.stdout = open(output_file, 'w')
#print(election_results1)