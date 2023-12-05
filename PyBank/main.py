
import os
import csv
import re
import statistics

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

def find_largest(dates_list, string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		large.append(numbers[i])

	max = large[0]
	for i in large:               
		if i > max:
			max = i
			maxDate = dates_list[i - 1]
	return (max)

def find_smallest(dates_list, string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		small.append(numbers[i])

	min = small[0]
	for i in small:               
		if i < min:
			min = i
			minDate = dates[i]
	return minDate, min


# -----------------------------------------------------------------------------------------


with open(profitLoss_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")

	csvHeader = next(csvfile)
	# print(f"Header: {csvHeader}")


# -----------------------------------------------------------------------------------------

# # Total Months: 86
	for row in csvReader:
		dates.append(row[0])
		profitLoss.append(row[1])

		tMonths = len(dates)

print(f"Total Months: " + str(tMonths))


# Total: $22564198
nProfitLoss = sum_numbers(profitLoss)

print(f"Total: " + "$ " + str((nProfitLoss)))


# Average Change: $-8311.11
average_change = sum_change(profitLoss)
monthsDiviser = tMonths - 1
print(f"Average Change: " + "$ " + str(round(int(sum(average_change)) / monthsDiviser, 2)))


# Greatest Increase in Profits: Aug-16 ($1862002)
dateOf, largestNumber = find_largest(dates, res)
print(f"str(largestNumber)"+ str(dateOf)+ " " + str(largestNumber))


# Greatest Decrease in Profits: Feb-14 ($-1825558)
smallest_Number = find_smallest(res)
print(f"str(smallestNumber)" + str(smallest_Number))


output_file = os.path.join("budgetResult.csv")




