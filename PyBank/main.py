import os
import csv

# Define input file and output file
input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('output.txt')

# Initialize variables
months = []
total_months = 0
net_pl = 0
monthly_pl = []
monthly_pl_diff = []
ave_pl_diff = 0
max_profit = 0
max_profit_month = ""
min_profit = 0
min_profit_month = ""


# Read input file
with open(input_path) as csv_input:
    reader = csv.reader(csv_input, delimiter=',')

    # Skip header
    next(reader)

    # Calculate total net P&L. Put monthly P&L in a list.  
    for row in reader:
        months.append(row[0])
        net_pl += int(row[1])
        monthly_pl.append(row[1])


# CALCULATIONS
# Total number of months in dataset
total_months = len(months)

# Differences in P&L from month-to-month
for i in range(total_months-1):
    monthly_pl_diff.append(int(monthly_pl[i+1]) - int(monthly_pl[i]))

# Average monthly difference in P&L
ave_pl_diff = sum(monthly_pl_diff)/len(monthly_pl_diff)

# Max profit difference and the month it occurred
max_profit = max(monthly_pl_diff)
max_profit_index = monthly_pl_diff.index(max_profit)
max_profit_month = months[max_profit_index+1]

# Min profit difference and the month it occurred
min_profit = min(monthly_pl_diff)
min_profit_index = monthly_pl_diff.index(min_profit)
min_profit_month = months[min_profit_index+1]


# Print results
results = f"----------------------------\nFinancial Analysis\n----------------------------\n"
results += f"Total Months: {total_months}\n"
results += f"Total: ${net_pl}\n"
results += f"Average Change: ${round(ave_pl_diff,2)}\n"
results += f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n"
results += f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})\n"
print(results)


# Write output file
with open(output_path, 'w') as output_file:
    output_file.write(results)
