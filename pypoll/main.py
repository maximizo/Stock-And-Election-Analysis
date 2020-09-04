#import os module
import os

#import module for reading csv file
import csv

#set path for csv file
csvpath = os.path.join('..', 'resources', 'PyPoll.csv')

#set variables
votes = 0
votecount = []
candidates = []
percentages = []

#open csv file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    #begin collecting data
    for row in csvreader:

        #calculate number of votes
        votes = votes + 1

        #identify candidate 
        candidate = row[2]

        #calculate votes per candidate
        if candidate in candidates:
            candidateid = candidates.index(candidate)
            votecount[candidateid] = votecount[candidateid] + 1
        
        else:
            candidates.append(candidate)
            votecount.append(int(1))

#calculate percentage of votes per candidate
mostvotes = votecount[0]
mostvotesid = 0
for count in range(len(candidates)):
    votepercent = (votecount[count]/votes)*100
    percentages.append(votepercent)

    #identify winner
    if votecount[count] > mostvotes:
        print(mostvotes)
        mostvotesid = count
winner = candidates[mostvotesid]


#print results
percentages = [round (i,5) for i in percentages]
print("Election Results")
print("--------------------------")
print(f'Total Votes:  {votes}')
print("--------------------------")
for count in range(len(candidates)):
    print(f'{candidates[count]}: {percentages[count]}% ({votecount[count]})')
print("--------------------------")
print("Winner: " + str(winner))
print("--------------------------")

#produce .txt file
with open('Election_Analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------\n")
    text.write(f'Total Votes:  {votes}\n')
    text.write("--------------------------\n")
    for count in range(len(candidates)):
        text.write(f'{candidates[count]}: {percentages[count]}% ({votecount[count]})')
        text.write("--------------------------\n")
        text.write("Winner: " + str(winner) + "\n")
        text.write("--------------------------\n")