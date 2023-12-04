
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


def sum_numbers(string_list):
	numbers = [int(num) for num in (string_list)]
	#print(numbers)
	return int(sum(numbers))
	
def sum_change(string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		res.append(numbers[i] - numbers[i-1])
	return int(sum(res))

def find_largest(string_list):
	numbers = [int(num) for num in (string_list)]
	for i in range(1, len(numbers)):
		large.append(numbers[i])
		max = large[(0)]
	print(int(large))
	

	# for i in large:
	# 	if max > int(large):
	# 		max = large
	# return int(max)


# def find_smallest(string_list):
# 	numbers = [int(num) for num in (string_list)]
# 	for i in range(1, len(numbers)):
# 		min = numbers[int(0)]
# 		if max < numbers:
# 			min = numbers
# 	return (min)




with open(profitLoss_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")

	csvHeader = next(csvfile)
	# print(f"Header: {csvHeader}")




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

print(f"Average Change: " + "$ " + str(round(average_change / monthsDiviser, 2)))


# Greatest Increase in Profits: Aug-16 ($1862002)

# largestNumber = find_largest(profitLoss)
# print(f"Greatest Increase in Profits: " + "$ " + str(largestNumber))


# Greatest Decrease in Profits: Feb-14 ($-1825558)

# smallestNumber = find_smallest(profitLoss)
# print(f"Greatest Decrease in Profits: " + "$ " + str(smallestNumber))



output_file = os.path.join("budgetResult.csv")




