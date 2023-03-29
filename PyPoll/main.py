import os.path
import csv

#make variables
votes_list = []
candidates_list = []
stockham = 0
degette = 0
doane = 0

#opening up the csv file to read and gather information from it
with open(r'C:\Users\Ryan Kracaw\Desktop\PyPoll\Resources\election_data.csv', 'r') as csvfile:
    csvreader = list(csv.reader(csvfile, delimiter=','))
    csv_header = next(csvreader
    for row in csvreader[1:]:
        votes_list.append(row[0])
        candidates_list.append(row[2])

#counts the candidates votes
for candidate in candidates_list:
    if candidate == 'Charles Casper Stockham':
        stockham += 1
    elif candidate == 'Diana DeGette':
        degette += 1
    elif candidate == 'Raymon Anthony Doane':
        doane += 1

#calculates the percent for candidates
stockham_percent = round((stockham/len(votes_list)) *100 ,3)
degette_percent = round((degette/len(votes_list)) *100 ,3)
doane_percent = round((doane/len(votes_list)) *100 ,3)

#lots of printing for the terminal analysis
print("Election Results")
print("-"*40)
print("Total Votes: " + str(len(votes_list)))
print("-"*40)
print("Charles Casper Stockham: " + str(stockham_percent) + "% " + str(stockham))
print("Diana DeGette: " + str(degette_percent) + "% " + str(degette))
print("Raymon Anthony Doane: " + str(doane_percent) + "% " + str(doane))
print("-"*40)

#finds the winner based on number of votes
if stockham > degette and stockham > doane:
    print("Winner: Charles Casper Stockham")
elif degette > stockham and degette > doane:
    print("Winner: Diana DeGette")
elif doane > stockham and doane > degette:
    print("Winner: Raymon Anthony Doane")

#writing to a text file
with open(r'C:\Users\Ryan Kracaw\Desktop\PyPoll\Analysis\output.txt', 'w') as target:
    target.write("Election Results")
    target.write("\n")
    target.write("-"*40)
    target.write("\n")
    target.write("Total Votes: ")
    target.write(str(len(votes_list)))
    target.write("\n")
    target.write("-"*40)
    target.write("\n")
    target.write("Charles Casper Stockham: ")
    target.write(str(stockham_percent))
    target.write("% ")
    target.write(str(stockham))
    target.write("\n")
    target.write("Diana DeGette: ")
    target.write(str(degette_percent))
    target.write("% ")
    target.write(str(degette))
    target.write("\n")
    target.write("Raymon Anthony Doane: ")
    target.write(str(doane_percent))
    target.write("% ")
    target.write(str(doane))
    target.write("\n")
    target.write("-"*40)
    target.write("\n")
    if stockham > degette and stockham > doane:
        target.write("Winner: Charles Casper Stockham")
    elif degette > stockham and degette > doane:
        target.write("Winner: Diana DeGette")
    elif doane > stockham and doane > degette:
        target.write("Winner: Raymon Anthony Doane")
