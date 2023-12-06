
import os
import csv
from collections import Counter


# collect data 
electionData_csv = os.path.join('Resources', 'election_data.csv')


ballots = []
counties = []
candidates = []
dct = {}
counter = {}
newDict = {}


list_of_lists = []

# -----------------------------------------------------------------------------------------

with open(electionData_csv) as csvfile:

	csvReader = csv.reader(csvfile, delimiter=",")
	csvHeader = next(csvfile)

	for row in csvReader:
		list_of_lists.append(row)

		ballots.append(row[0])
		counties.append(row[1])
		candidates.append(row[2])

	# turn list into dictionary as keys. dictionaries can't have keys  www.w3school.com		
electionResults = list( dict.fromkeys(candidates))
number_of_candidates = len(electionResults)



	# from realpython.com/python-counter/
electionResults = Counter(candidates)

winnerIs = Counter(candidates).most_common(1)[0][0]


# # -----------------------------------------------------------------------------------------

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
print(f"Total Votes: " + str(len(ballots)))
print(f"")
print(f'-------------------------------------------------------------')
print(f"")

for key, value in electionResults.items():
	print(key, value, format(value/len(ballots), '.2%'))

print(f"")

print(f'-------------------------------------------------------------')

print(f'The Winner is : ' + winnerIs)
print(f'-------------------------------------------------------------')
print(f"")

# -----------------------------------------------------------------------------------------


# output_file = os.path.join("electionResult.csv")

# with open('electionResult.csv', 'w', newline='') as file:
# 	writer = csv.writer(file)

# 	writer.writerow(["Election Results"])
# 	writer.writerow([])
# 	writer.writerow(["------------------------------------------------------"])
# 	writer.writerow([])
# 	writer.writerow(["Total Votes: " + str(len(ballots))])
# 	writer.writerow([])
# 	writer.writerow(["------------------------------------------------------"])
# 	writer.writerow([])
#  	writer.writerow([])
#  	writer.writerow(['The Winner is : ' + winnerIs])
# 	writer.writerow([])
# 	writer.writerow(["------------------------------------------------------"])



































