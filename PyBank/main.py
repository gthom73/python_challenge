
import os
import csv
# import re
# import statistics

# collect data 
profitLoss_csv = os.path.join('Resources', 'budget_data.csv')


dates = []
profitLoss = []
nProfitLoss = 0.0
average_change = 0.0
res = []
large = []
small = []

# -----------------------------------------------------------------------------------------

with open(profitLoss_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")
	csvHeader = next(csvfile)

	for row in csvReader:
		dates.append(row[0])
		profitLoss.append(row[1])
		tMonths = len(dates)

with open(profitLoss_csv, mode='r') as csvfileII:
	csvReaderII = csv.reader(csvfileII)
	csvHeaderII = next(csvfileII)

	with open('profitLoss_csv', mode='w') as plOutFile:
		writer = csv.writer(plOutFile)
		profitLossDict = {rows[0]:rows[1] for rows in csvReaderII}


# print(profitLossDict)

# -----------------------------------------------------------------------------------------

def sum_numbers(string_list):
	numbers = [int(num) for num in (string_list)]
	#print(numbers)
	return int(sum(numbers))
	
def sum_change(string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		res.append(int(numbers[i] - numbers[i-1]))
		ressum = int(sum(res))
	return res

# -----------------------------------------------------------------------------------------


def find_largest(string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		large.append(numbers[i])

	max = large[0]
	for i in large:               
		if i > max:
			max = i
	return max

def find_smallest(string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		small.append(numbers[i])

	min = small[0]
	for i in small:               
		if i < min:
			min = i
	return min

# -----------------------------------------------------------------------------------------
print(f"")
print(f"")
print(f"")
print(f"Financial Analysis")
print(f"")
print(f'-------------------------------------------------------------')
print(f"")


# # Total Months: 86
print(f"Total Months: " + str(tMonths))

print(f"")
# Total: $22564198
nProfitLoss = sum_numbers(profitLoss)

print(f"Total: " + "$ " + str(nProfitLoss))

print(f"")
# Average Change: $-8311.11
average_change = sum_change(profitLoss)
monthsDiviser = tMonths - 1
print(f"Average Change: " + "  $ " + str(round(int(sum(average_change)) / monthsDiviser, 2)))
print(f"")

# # Greatest Increase in Profits: Aug-16 ($1862002)
largestNumber = find_largest(res)
print(f"Greatest Increase in Profits:" + "  $ " + str(largestNumber))
print(f"")

# # Greatest Decrease in Profits: Feb-14 ($-1825558)
smallestNumber = find_smallest(res)
print(f"Greatest Decrease in Profits:" + "  $ " + str(smallestNumber))
print(f"")
print(f"")
print(f"")

output_file = os.path.join("budgetResult.csv")

with open('budgetResult.csv', 'w', newline='') as file:
	writer = csv.writer(file)

	writer.writerow(["Financial Analysis"])
	writer.writerow([])
	writer.writerow(["------------------------------------------------------"])
	writer.writerow([])
	writer.writerow(["Total Months: " + str(tMonths)])
	writer.writerow([])
	writer.writerow(["Total: " + "  $ " + str(nProfitLoss)])
	writer.writerow([])
	writer.writerow(["Average Change: " + "  $ " + str(round(int(sum(average_change)) / monthsDiviser, 2))])
	writer.writerow([])
	writer.writerow(["Greatest Increase in Profits:" + "  $ " + str(largestNumber)])
	writer.writerow([])
	writer.writerow(["Greatest Decrease in Profits:" + "  $ " + str(smallestNumber)])



































