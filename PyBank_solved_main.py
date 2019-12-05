# Import the Modules 
import csv, os

# Function to add both columns from the csv files to individual lists
def adding_Elements(month_pro):
	# Adding the Month-Year of the row to the list 
	all_months.append(str(month_pro[0]))   	
	
	# Adding the Profit of the row to the list  	
	all_profits.append(int(month_pro[1]))
	
	return 

# Function to compute the Profit change from previous month to next(current) month 
def change_InProfit(bud_pro, old_profit):
	# local variable to hold profit difference 
	profit_difference = 0 
	 
	# If-else statement to assign previous row as old profit, current row as new profit if it is not the first row  	
	if str(bud_pro[0]) == 'Jan-2010':
		new_profit = int(bud_pro[1])
		return new_profit 
	else: 
		new_profit = int(bud_pro[1])
		profit_difference = new_profit - old_profit
		profit_changes.append(profit_difference)

		# Adding the respective profit change and new month to the list  
		months_profit_changes.append([str(bud_pro[0]), profit_difference]) 
		
		#Return the new profit difference back to be used as the previous profit difference next time  
		return new_profit

# Function to compute the overall average profit change of all the rows
def average_Profit(avg_pro):
	# local variable storing the average  
	average_change = 0 
	
	# Calculate the average  
	average_change = sum(avg_pro)/len(avg_pro)

	# Return the average change to the nearest 2 decimals 
	return (round(average_change,2))

# Function to find the greatest increase in profit and return the month-profit difference in a dictionary
def greatest_Increase(mo_diff):
 	# local variable to store maximum increase
	max_change= 0
	diction = {}  
	# Set local maximum profit change using the first row
	max_change = mo_diff[0][1]			

	# Loop through the multi-dimensional list to find greatest increase and its respective month 
	for row in mo_diff:
		if row[1] > max_change:	
			# Storing the temporary dictionary 
			diction = {row[0]:row[1]}
		
			# Replace the local variables 
			max_change = row[1]

	return diction 

# Function to find the greatest decrease in profit and return the month-profit difference in a dictionary
def greatest_Decrease(mo_diff):
	# local variables to store maximum decline
	min_change = 0
	diction2 = {}
	# Set local minimum profit change using the first row
	min_change = mo_diff[0][1]		

	# Loop through the multi-dimensional list to find greatest increase and its respective month 
	for row in mo_diff:
		if row[1] < min_change:
			# Storing the temporary dictionary 
			diction2 = {row[0]:row[1]}
			
			# Replace the local variables 
			min_change = row[1]

	return diction2

# Function to return a single key from dictionary without brackets, parenthesis, or quotations 
def pull_Key(dict_pair):
	for key in dict_pair.keys():
		return key

# # Function to return a single value from dictionary without brackets, parenthesis, or quotations 
def pull_Value(dict_pair):
	for value in dict_pair.values():
		return value


# Path to the budget data csv file, retracking one directory 
budget = os.path.join("..", "Resources", "budget_data.csv")

# Defining new variables 
new_profit, avg_change = 0, 0
max_increase, month_increase = 0, 0 
max_decrease, month_decrease = 0, 0    
all_months = []
all_profits = []
profit_changes = []
months_profit_changes = [] 
temp_dict, temp_dict2 = {}, {}

# Opening the budget_data csv file 
with open(budget, 'r', newline="") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",") 
	
	# Exclude the header before continuing 
	header = next(csv_reader) 
	
	# Loop to count the number of rows and calculate the profit change month by month   
	for row in csv_reader:  		
	 	
		# Adding each rows elements 
		adding_Elements(row)	
	
		# Computing the profit difference 
		new_profit = change_InProfit(row, new_profit)
		
	# Computing the average profit change 
	avg_change = average_Profit(profit_changes)
	
	# Finding the maximum profit increase change 
	temp_dict = greatest_Increase(months_profit_changes) 
	
	# Finding the maximum profit decline change 
	temp_dict2 = greatest_Decrease(months_profit_changes)

	# Pull out the individual values from the dictionary 
	month_increase = pull_Key(temp_dict)
	max_increase = pull_Value(temp_dict)
	month_decrease = pull_Key(temp_dict2)
	max_decrease = pull_Value(temp_dict2)

# Printing out the expected output 
print(f'\n```text\n'
	f'Financial Analysis\n'
	f'-----------------------\n'
	f'Total Months: {len(all_months)}\n'
	f'Total: ${sum(all_profits)}\n'
	f'Average Change: ${avg_change}\n'
	f'Greatest Increase in Profits: {month_increase} (${max_increase})\n'
	f'Greatest Decrease in Profits: {month_decrease} (${max_decrease})\n'
	f'```') 

# Create and open the text file to write in 
writer = open("PyBank_newfile.txt", 'w')

#Write in the expected output with the results  
writer.write(f'```text\n')
writer.write(f'Financial Analysis\n') 
writer.write(f'-----------------------\n')
writer.write(f'Total Months: {len(all_months)}\n')
writer.write(f'Total: ${sum(all_profits)}\n')
writer.write(f'Average Change: ${avg_change}\n')
writer.write(f'Greatest Increase in Profits: {month_increase} (${max_increase})\n')
writer.write(f'Greatest Decrease in Profits: {month_decrease} (${max_decrease})\n')
writer.write(f'```') 

# Close the file 
writer.close()
