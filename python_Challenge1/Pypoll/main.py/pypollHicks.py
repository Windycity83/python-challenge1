# Modules
import csv
# Set path for file
csvpath = "PyPoll/Resources/election_data.csv"
# Initialize variables
vote_count = 0
candidate_dict = {}
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # Count votes
        vote_count += 1
        # Add to dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1
    print(vote_count)
    print(candidate_dict)
    # shout out to the Xpert for helping me through this and fixing my errors
   # Create our output
output = f"""Election Results
-------------------------
Total Votes: {vote_count}
-------------------------
"""
max_cand = ""
max_votes = 0
for candidate in candidate_dict.keys():
    # get votes
    votes = candidate_dict[candidate]
    perc = 100 * (votes / vote_count)
    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line
    # get max of dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes
last_line = f"""-------------------------
Winner: {max_cand}
-------------------------
"""
output += last_line
print(output)
# xpert does it again fixing my indentations






