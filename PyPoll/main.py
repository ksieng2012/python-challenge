#Import Required packages
import os
import csv
import copy


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
    # print(cand_list)


    #   * The percentage of votes each candidate won
    #   * The total number of votes each candidate won
    for i in range(0,len(cand_list)):
        
        for j in range(0,len(candidate)):
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

    # Counter decending index
    coun_array_dece = coun_array.copy()
    coun_i_dece = []
    # sort decending list
    for i in range(0, len(coun_array_dece)):
        for j in range(i+1, len(coun_array_dece)):
            if coun_array_dece[i] < coun_array_dece[j]:
                temp = coun_array_dece[i]
                coun_array_dece[i] = coun_array_dece[j]
                coun_array_dece[j] = temp

    #  finding decending index for the vot count
    temp_idex =0
    for i in range(len(coun_array_dece)):
        for j in range(len(coun_array)):
            if coun_array[j] == coun_array_dece[i]:
                temp_index = j
        coun_i_dece.append(temp_index)
        temp_index = 0

#   * The winner of the election based on popular vote.
win_can = cand_list[max_i]

# * As an example, your analysis should look similar to the one below:
win_list=[]
for i in range(len(cand_list)):
    a=int(coun_i_dece[i])
    win_list.append(str(f'{cand_list[a]}: {"{:.2f}".format(perc_array[a])}% ({coun_array[a]}) '))

# print(win_list)

print(f'''
Election Results
-------------------------
Total Votes : {total_votes} ''')
for i in range(len(cand_list)):
    a=int(coun_i_dece[i])
    print(f'{cand_list[a]}: {"{:.2f}".format(perc_array[a])}% ({coun_array[a]}) ')
print(f'''-------------------------
Winner : {win_can}
-------------------------''')



# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_path = os.path.join("Result.txt")

with open(output_path, 'w', newline='') as f:
    f.write(f'''Election Results \n-------------------------\nTotal Votes : {total_votes}\n{win_list[0]}\n{win_list[1]}\n{win_list[2]}\n{win_list[3]}\n''')

    f.write(f'''-------------------------\nWinner : {win_can}\n-------------------------''')