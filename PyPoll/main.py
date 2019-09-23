import os
import csv
from collections import Counter

# Define input file and output file
input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('output.txt')

# Initialize variables
total_votes = 0
all_candidates = []


# Read input file
with open(input_path) as csv_input:
    reader = csv.reader(csv_input, delimiter=',')

    #Skip header
    next(reader)

    # Total votes and make a list of candidates
    for row in reader:
        total_votes += 1
        all_candidates.append(row[2])


# Count votes per candidate, automatically ordered by ascending
candidate_counter = Counter(all_candidates)
candidates = tuple(candidate_counter.keys())
votes = tuple(candidate_counter.values())


# Poll results
poll_results = "Election Results\n-------------------------\n"
poll_results += f"Total Votes: {total_votes}\n-------------------------\n"

# Loop to include all candidates
for i in range(len(candidates)):
    votes_formatted = "{:.3%}".format(votes[i]/total_votes)
    poll_results += f"{candidates[i]}: {votes_formatted}% ({votes[i]})\n"

# Winner
poll_results += f"-------------------------\nWinner: {candidates[0]}\n-------------------------"

# Print to terminal
print(poll_results)


# Write output file
with open(output_path, 'w') as output_file:
    output_file.write(poll_results)
