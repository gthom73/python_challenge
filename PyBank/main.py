
import os
import csv

# collect data 
profitLoss_csv = os.path.join('Resources', 'budget_data.csv')


dates = []
profitLoss = []

with open(profitLoss_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")

	for 






	# for row in csvReader:
	# 	dates.append(rows[])

	# csv_header = next(csvReader)

	# print(f"CSV Header: {csvReader}")

	# for row in csvReader:










	# 	print(row)

# # define the fuction and have it accept the p/l information
# def print_financialSummary(pl_data):

# 	month = str(pl_data[0])
# 	monthpl = int(pl_data[1])


# # Financial Analysis

# #--------------------------------

# # Total Months: 86
# 	total_months = len(month)
# 	print(f"Total Months:")

# Total: $22564198

# Average Change: $-8311.11

# Greatest Increase in Profits: Aug-16 ($1862002)

# Greatest Decrease in Profits: Feb-14 ($-1825558)

