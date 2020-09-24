#Import Required packages
import os
import csv


# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of 
# three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates 
# each of the following:

# Read CSV files
csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)

with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    # Read the header row first. and remove it from the data
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    data = list(csvreader)
    unzip_data=list(zip(*data))
    voter_id = unzip_data[0]
    county = unzip_data[1]
    candidate = unzip_data[2]
    # print(candidate[1:10])

#   * The total number of votes cast
    total_votes = len(voter_id)
    # print(total_vote)

#   * A complete list of candidates who received votes
    # list of candidates
    cand_list = list(set(candidate))
    # print(cand_list)
    coun_array = []
    perc_array = []
    counter=0


    #   * The percentage of votes each candidate won
    #   * The total number of votes each candidate won
    for i in range(len(cand_list)):
        
        for j in range(len(candidate)):
            if candidate[j]==cand_list[i]:
                counter= counter+1
        # print(counter)
        coun_array.append(counter)
        perc_array.append(counter/total_votes*100)
        counter=0
    # print(perc_array)
    max_i=[i for i in range(len(coun_array)) if coun_array[i] == max(coun_array)]
    max_i=int(max_i[0])
    # print(coun_array)
    # print(max_i)

# # Arange winning index
# # coun_array_sort = coun_array.sort(reverse=True)
# print(coun_array)

# for i in range(len(coun_array)):

    
#   * The winner of the election based on popular vote.
win_can = cand_list[max_i]
# * As an example, your analysis should look similar to the one below:

print('Election Results')
print('-------------------------')
print(f'Total Votes : {total_votes}')
print('-------------------------')
for i in range(len(cand_list)):
    print(f'{cand_list[i]}: {"{:.2f}".format(perc_array[i])}% ({coun_array[i]}) ')
print('-------------------------')
print(f'Winner : {win_can}')
print('-------------------------')

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.