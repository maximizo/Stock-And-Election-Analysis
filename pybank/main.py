#import os module 
import os

#import module for reading csv file
import csv

#set path for csv file
csvpath = os.path.join('..','resources','PyBank.csv')

#set data lists
profit = []
monthlychange = []
date = []

#set variables
totalmonths = 0
totalprofit = 0
totalprofitchange = 0
beginningprofit = 0

#open the csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip the header
    csvheader = next(csvreader)

    #begin collecting data
    for row in csvreader:
        
        #count the total number of months
        totalmonths = totalmonths + 1

        #capture data for finding greatest profit and greatest loss
        date.append(row[0])

        #calculate total profit
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])

        #calculate avg monthly profit change
        finalprofit = int(row[1])

        #calculate total avg profit change 
        monthlyprofitchange = finalprofit - beginningprofit

        #save monthly changes in a list
        monthlychange.append(monthlyprofitchange)
        totalprofitchange = (totalprofitchange + monthlyprofitchange)
        beginningprofit = finalprofit

        #calculate avg change in profits over entire period
        avgprofitchange = round(monthlyprofitchange/totalmonths,2)

        #find the greatest profit and greatest loss
        greatestprofit = max(monthlychange)
        greatestloss = min(monthlychange)
        greatestprofitdate = date[monthlychange.index(greatestprofit)]
        greatestlossdate = date[monthlychange.index(greatestloss)]

    #print results
    print("Financial Analysis")
    print("--------------------------")
    print("Toal Months: " + str(totalmonths))
    print("Total: $" + str(totalprofit))
    print("Average Change: $" + str(int(avgprofitchange)))
    print("Greatest Increase in Profits: " + str(greatestprofitdate) + " ($" + str(greatestprofit) + ")")
    print("Greatest Decrease in Profits: " + str(greatestlossdate) + " ($" + str(greatestloss) + ")")

#Produce .txt file
with open('Financial_Analysis.txt','w') as text:
    text.write("Financial Analysis\n")
    text.write("--------------------------\n")
    text.write("Total Months: " + str(totalmonths) + "\n")
    text.write("Total: $" + str(totalprofit) + "\n")
    text.write("Average Change: $" + str(int(avgprofitchange)) + "\n")
    text.write("Greatest Increase in Profits: " + str(greatestprofitdate) + " ($" + str(greatestprofit) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(greatestlossdate) + " ($" + str(greatestloss) + ")\n")

