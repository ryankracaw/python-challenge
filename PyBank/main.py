import os.path
import csv

# making vaiables
months_list = []
money = 0
change =[]
the_sum = 0
diff = []

#opening up the csv file to read and gather information from it
with open(r'C:\Users\Ryan Kracaw\Desktop\PyBank\Resources\budget_data.csv', 'r') as csvfile:
    csvreader = list(csv.reader(csvfile, delimiter=','))
    for row in csvreader[1:]: #the [1:] skips the first row since that is a header
        months_list.append(row[0]) #makes a list of the months for later use
        money = money + int(row[1]) #sums up the profits/loses
        change.append(int(row[1])) #makes a list of the profits/loses for a later use
        
months = len(months_list) #gets the length of the months list to get the total months

for i, j in zip(change[:-1], change[1:]): #this for loop takes the second element then subtracts it from the first to find the difference
    diff.append(j-i) #makes a list of these differences
for cell in diff: #this for loop is going to sum those differences in order to calculate the average
    the_sum = sum(diff)
average = str(round((the_sum)/len(diff),2)) #finds the average and rounds

max_value = max(diff) #gets max value
min_value = min(diff) #gets min value

for i in range(len(diff)): #this for loop is going to find which months had the greatest increase or decrease
    if max_value == diff[i]: #checking max value first
        max_date = str(months_list[i+1]) #since we subtracted the second element from the first in the loop above, our indexing is off by 1
    elif min_value == diff[i]:
        min_date = str(months_list[i+1])

#lots of printing for the terminal analysis
print("Financial Analysis")
print("-"*40)

print("Total months: ", months)
print("Total: " + " $" + str(money))
print("Average Change: " + " $" + str(average))
print("Greatest Increase in Profits: " + max_date + " ($" + str(max_value) + ")")
print("Greatest Decrease in Profits: " + min_date + " ($" + str(min_value) + ")")

#writing to a text file
with open(r'C:\Users\Ryan Kracaw\Desktop\PyBank\Analysis\output.txt', 'w') as target:
    target.write("Financial Analysis")
    target.write("\n")
    target.write("-"*40)
    target.write("\n")
    target.write("Total months: ")
    target.write(str(months))
    target.write("\n")
    target.write("Average Change: $")
    target.write(str(money))
    target.write("\n")
    target.write("Average Change: $")
    target.write(str(average))
    target.write("\n")
    target.write("Greatest Increase in Profits: ")
    target.write(max_date)
    target.write(" $")
    target.write(str(max_value))
    target.write("\n")
    target.write("Greatest Increase in Profits: ")
    target.write(min_date)
    target.write(" $")
    target.write(str(min_value))

