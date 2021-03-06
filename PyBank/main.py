#imports
import os

import csv

#join correct path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Lists to store data
totMonth = []
netTot = []
changes = []
maxProf = []
dates = []
minProf = []

#finding total months
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    #Variables start
    number = 0 
    nxt_number = 0
    diff_in = 0
    aveChange = 0 
    row_amount = 0
    netTot = 0
    inc_dec = 0

    csv_header = next(csvfile)
    
    totMonth = list(csvfile)
    overall_month = len(totMonth)
    ave_overall_month = ((overall_month)-1)

    print(f" ")
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {overall_month}")

#find the total average and increases/decreases
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csv_reader:

        maxProf.append (float(row[1]))
        dates.append(str(row[0]))
        minProf.append (float(row[1]))
        row_amount = row_amount + int(row[1])
        sticker = str(max(row[1]))
        #print (row_amount)
        if number == 0:
            number = int(row[1])
        else:
            nxt_number = int(row[1])
            diff_in = (nxt_number-number)
            nxt_number = number
        if row[1] == maxProf:
                dates = row[0]
    print("Total: " + "$" + str(row_amount))
    aveChange = round((diff_in)/(ave_overall_month),2)
    print("Average Change: " + "$" + str(aveChange))
    print("Greatest Increase in Profits: " + row[0] + " " + "($" + str(max(maxProf)) + ")")
    print("Greatest Decrease in Profits: " + row[0] + " " + "($" + str(min(minProf)) + ")")

 
print(f" ")

#output file
output_file = os.path.join("Analysis", "P_N_L.csv")
with open(output_file, "w", newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerow(["Total Months", str(overall_month)])
    writer.writerow(["Total", "$" + str(row_amount)])
    writer.writerow(["Average Change", "$" + str(aveChange)])
    writer.writerow(["Greatest Increase", row[0] + " " + "$" + str(max(maxProf))])
    writer.writerow(["Greatest Decrease", row[0] + " " + "$" + str(min(minProf))])
    