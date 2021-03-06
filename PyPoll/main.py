#imports
import os
import csv

#join current path
election_csv = os.path.join("Resources", "election_data.csv")

#Initiating list variables
tot_votes = []
totalVotes = []
candidates = []
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
khan_perc = 0
correy_perc = 0
li_perc = 0
otooley_perc = 0

#finding total votes
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    tot_votes = list(csvfile)
    totalVotes = len(tot_votes)

    print(f"")
    print(f"Election Results")
    print(f"-----------------------")
    print(f"Total Votes: {totalVotes}")
    print(f"-----------------------")
    
#Finding vote amounts and percentages
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        candidates.append(row[2])
        if row[2] == "Khan":
            khan_vote += 1
        if row[2] == "Correy":
            correy_vote += 1
        if row[2] == "Li":
            li_vote += 1
        if row[2] == "O'Tooley":
            otooley_vote += 1
    
    khan_perc = round((khan_vote / totalVotes)*100,3)
    correy_perc = round((correy_vote / totalVotes)*100,3)
    li_perc = round((li_vote / totalVotes)*100,3)
    otooley_perc = round((otooley_vote / totalVotes)*100,3) 

    print(f"Khan: {khan_perc}% ({khan_vote})")
    print(f"Correy: {correy_perc}% ({correy_vote})")
    print(f"Li: {li_perc}% ({li_vote})")
    print(f"O'Tooley: {otooley_perc}% ({otooley_vote})")
    print(f"-----------------------")

#if statements to see who won
    if khan_vote > correy_vote and li_vote and otooley_vote:
        print(f"Winner: Khan")
    if correy_vote > khan_vote and li_vote and otooley_vote:
        print(f"Winner: Correy")
    if li_vote > correy_vote and khan_vote and otooley_vote:
        print(f"Winner: Li")
    if otooley_vote > correy_vote and li_vote and khan_vote:
        print(f"Winner: O'Tooley")

    print(f"-----------------------")
    print(f"")

#output file
output_file = os.path.join("Analysis", "E-Lection.csv")
with open(output_file, "w", newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerow(['Candidates', 'Percentage', 'Total Vote'])
    writer.writerow(['Khan', str(khan_perc), str(khan_vote)])
    writer.writerow(['Correy', str(correy_perc), str(correy_vote)])
    writer.writerow(['Li', str(li_perc), str(li_vote)])
    writer.writerow(['OTooley', str(otooley_perc), str(otooley_vote)])
