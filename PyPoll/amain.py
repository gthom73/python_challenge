
import os
import csv
# import re
# import statistics

# total number of votes cast   369711

# complete list of candidates who received votes

# perccentage of votes each candidate won
# total number of votes each candidate won
# winner of the election based on popular vote



# collect data 
electionData_csv = os.path.join('Resources', 'election_data.csv')


ballotID = []
county = []
candidate = []

nProfitLoss = 0.0
average_change = 0.0
res = []
large = []
small = []

# -----------------------------------------------------------------------------------------

with open(electionData_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")
	csvHeader = next(csvfile)

	for row in csvReader:
		ballotID.append(row[0])
		county.append(row[1])
		candidate.append(row[2])
		

print(f'Candidate list looks like this', candidate)











# def candidates_names(candidateList)
# 	numbers = [int(num) for num in (candidateList)]
# 	for i in range(1, len(numbers)):


# with open(electionData_csv, mode='r') as csvfileII:
# 	csvReaderII = csv.reader(csvfileII)
# 	# with header = yes
# 	csvHeaderII = next(csvfileII)

# 	with open('electionData_csv', mode='w') as plOutFile:
# 		writer = csv.writer(plOutFile)
# 		electionDataDict = {rows[0]:rows[1],rows[1]} for rows in csvReaderII


#print(tvotes)
# print(electionDataDict)


# # -----------------------------------------------------------------------------------------

# def sum_numbers(string_list):
# 	numbers = [int(num) for num in (string_list)]
# 	#print(numbers)
# 	return int(sum(numbers))
	
# def sum_change(string_list):
# 	numbers = [int(num) for num in (string_list)]
# 	for i in range(1, len(numbers)):
# 		res.append(int(numbers[i] - numbers[i-1]))
# 		ressum = int(sum(res))
# 	return res

# # -----------------------------------------------------------------------------------------


# def find_largest(string_list):
# 	numbers = [int(num) for num in (string_list)]
# 	for i in range(1, len(numbers)):
# 		large.append(numbers[i])

# 	max = large[0]
# 	for i in large:               
# 		if i > max:
# 			max = i
# 	return max

# def find_smallest(string_list):
# 	numbers = [int(num) for num in (string_list)]
# 	for i in range(1, len(numbers)):
# 		small.append(numbers[i])

# 	min = small[0]
# 	for i in small:               
# 		if i < min:
# 			min = i
# 	return min

# -----------------------------------------------------------------------------------------
print(f"")
print(f"")
print(f"")
print(f"Election Results")
print(f"")
print(f'-------------------------------------------------------------')
print(f"")


# # total votes 369711
print(f"Total Votes: " + str(len(ballotID)))
print(f"")
print(f'-------------------------------------------------------------')
print(f"")
# print(f"")
# # Total: $22564198
# nProfitLoss = sum_numbers(profitLoss)

# print(f"Total: " + "$ " + str(nProfitLoss))

# print(f"")
# # Average Change: $-8311.11
# average_change = sum_change(profitLoss)
# monthsDiviser = tMonths - 1
# print(f"Average Change: " + "  $ " + str(round(int(sum(average_change)) / monthsDiviser, 2)))
# print(f"")

# # # Greatest Increase in Profits: Aug-16 ($1862002)
# largestNumber = find_largest(res)
# print(f"Greatest Increase in Profits:" + "  $ " + str(largestNumber))
# print(f"")

# # # Greatest Decrease in Profits: Feb-14 ($-1825558)
# smallestNumber = find_smallest(res)
# print(f"Greatest Decrease in Profits:" + "  $ " + str(smallestNumber))
# print(f"")
# print(f"")
# print(f"")

# output_file = os.path.join("budgetResult.csv")

# with open('budgetResult.csv', 'w', newline='') as file:
# 	writer = csv.writer(file)

# 	writer.writerow(["Election Results"])
# 	writer.writerow([])
# 	writer.writerow(["------------------------------------------------------"])
# 	writer.writerow([])
# 	writer.writerow(["Total Votes: " + str(len(ballotID))])
# 	writer.writerow([])
# 	writer.writerow(["Total: " + "  $ " + str(nProfitLoss)])
# 	writer.writerow([])
# 	writer.writerow(["Average Change: " + "  $ " + str(round(int(sum(average_change)) / monthsDiviser, 2))])
# 	writer.writerow([])
# 	writer.writerow(["Greatest Increase in Profits:" + "  $ " + str(largestNumber)])
# 	writer.writerow([])
# 	writer.writerow(["Greatest Decrease in Profits:" + "  $ " + str(smallestNumber)])



































