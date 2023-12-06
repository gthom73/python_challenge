
import os
import csv
from collections import Counter


# collect data 
electionData_csv = os.path.join('Resources', 'election_data.csv')

list_of_lists = []
ballots = []
counties = []
candidates = []
counter = {}

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
# Wanted to write this information to a new dictionary
# couldn't get it to happen.

print(f"")
print(f'-------------------------------------------------------------')
print(f'The Winner is : ' + winnerIs)
print(f'-------------------------------------------------------------')
print(f"")

# -----------------------------------------------------------------------------------------


output_file = os.path.join("electionResult.csv")

with open('electionResult.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Election Results"])
	writer.writerow([])
	writer.writerow(["------------------------------------------------------"])
	writer.writerow([])
	writer.writerow(["Total Votes: " + str(len(ballots))])
	writer.writerow([])
	writer.writerow(["------------------------------------------------------"])
	writer.writerow([])
	writer.writerow([])
	writer.writerow(["Did not get a handle on writing a dictionary to"])
	writer.writerow(["a dictionary. Would have liked to write out"])
	writer.writerow(["priint(key, value, format(value/len(ballots), '.2%''))"])
	writer.writerow(["to a new dictionary and then print that dictionary here."])
	writer.writerow([])
	writer.writerow(["------------------------------------------------------"])
	writer.writerow([])
	writer.writerow(['The Winner is : ' + winnerIs])	
	writer.writerow([])
	writer.writerow(["------------------------------------------------------"])
































