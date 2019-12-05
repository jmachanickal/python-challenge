# Importing the Modules 
import csv, os

def add_Elements(vote):
	# Adding the Candidate of the row to the list  	
	all_candidates.append(str(vote[2]))
	return 

def count_Votes(vote): 
	if vote[2] == 'Correy':
		vote_correy.append(vote[0])
	elif vote[2] == 'Khan':
		vote_khan.append(vote[0])
	elif vote[2] == 'Li':
		vote_li.append(vote[0])
	else:
		vote_tool.append(vote[0])
		
	return 

# Function to return the percentage of votes won by a candidate 
def get_Percent(candidate_votes):
	return round(len(candidate_votes)/len(all_candidates)*100,3)

# Function to return the winner of the election 
def winning_Candidate(thow):
	# Set up local variables as default   
	set_winner, winner = 0, 0  
	
	for key, value in thow.items(): 
		if value[0] > set_winner:
			set_winner = value[0]
			winner = key
				
	return winner 

# Function to sort the dictionary by values in reverse order  
def sort_Polls(poll):
	return sorted(poll.items(), key = lambda kv: kv[1], reverse=True)	

# Path to the budget data csv file, retracking one directory 
election = os.path.join("..", "Resources", "election_data.csv")

# Defining new variables
poll_winner, percent_correy, percent_khan, percent_li, percent_tool = 0, 0, 0, 0, 0  
all_candidates, vote_correy, vote_khan, vote_li, vote_tool = [], [], [], [], []
results, results_sorted = {}, {} 

# Opening the budget_data csv file 
with open(election, 'r', newline="") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",") 
	# Exclude the header before continuing 
	header = next(csv_reader) 
	
	# Loop to count the total number of votes and voting count for each candidate    
	for row in csv_reader:  		
		add_Elements(row)
		count_Votes(row)
	
	# Get percentage of votes for each candidate 
	percent_correy = get_Percent(vote_correy)	
	percent_khan = get_Percent(vote_khan)
	percent_li = get_Percent(vote_li)
	percent_tool = get_Percent(vote_tool)

	# Set up a dictionary of lists 
	results = {"Correy": [percent_correy, len(vote_correy)],
		  "Khan": [percent_khan, len(vote_khan)],
		  "Li": [percent_li, len(vote_li)],
		  "O' Tooley": [percent_tool, len(vote_tool)]}	
	
	# Send dictionary of lists to function to find the winner 
	poll_winner = winning_Candidate(results)
	
	# Sort the dictionary 
	results_sorted = sort_Polls(results) 
	
	# Printing out the expected output 
	print(f'\n```text')
	print(f'Election Results')
	print(f'--------------------------')
	print(f'Total Votes: {len(all_candidates)}')	
	print(f'--------------------------')
	for key, value in results_sorted:
		print(f'{key}: {value[0]}% ({value[1]})') 	
	print(f'--------------------------')
	print(f'Winner: {poll_winner}')
	print(f'--------------------------')
	print(f'```')

	# Create and open the text file to write in 
	writer = open("PyPoll_newfile.txt", 'w')

	#Write in the expected output with the results  
	writer.write(f'\n```text\n')
	writer.write(f'Election Results\n')
	writer.write(f'--------------------------\n')
	writer.write(f'Total Votes: {len(all_candidates)}\n')	
	writer.write(f'--------------------------\n')
	for key, value in results_sorted:
		writer.write(f'{key}: {value[0]}% ({value[1]})\n') 	
	writer.write(f'--------------------------\n')
	writer.write(f'Winner: {poll_winner}\n')
	writer.write(f'--------------------------\n')
	writer.write(f'```\n')

	# Close the file 
	writer.close()