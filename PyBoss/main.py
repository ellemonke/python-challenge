import os
import csv
import string

# Import U.S. states dictionary
import us_state_abbrev
us_states = us_state_abbrev.us_state_abbrev

# Define input file and output file
input_path = os.path.join('employee_data.csv')
output_path = os.path.join('employee_data_formatted.csv')

# Initialize lists for every column in output file
emp_id = []
full_names = []
first_names = []
last_names = []
dob = []
ssn = []
state = []
counter = 0

# Function to format date from YYYY-MM-DD to MM/DD/YYYY
def date_format(date):
    split_date = []
    split_date = date.split('-')
    new_date = split_date[1] + "/" + split_date[2] + "/" + split_date[0]
    return new_date

# Function to show only the last 4 digits of SSN numbers 
def ssn_anon(ssn):
    split_ssn = ssn.split('-')
    new_ssn_list = ["***-**-"]
    new_ssn_list.append(split_ssn[2])
    new_ssn = ''.join(new_ssn_list)
    return new_ssn

# Function to format state names to their two-letter abbreviation
def state_abbrev(state):
    state_abbrev = us_states.get(state)
    return state_abbrev

# Open input file
with open(input_path) as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')

    # Read every row and format info
    for row in reader:
        emp_id.append(row['Emp ID'])
        full_names.append(row['Name'].split(' ',1))
        first_names.append(full_names[counter][0])
        last_names.append(full_names[counter][1])
        dob.append(date_format(row['DOB']))
        ssn.append(ssn_anon(row['SSN']))
        state.append(state_abbrev(row['State']))
        counter += 1

# Zip all newly formatted lists into one structure
formatted = zip(emp_id, first_names, last_names, dob, ssn, state)

# Create output CSV file
with open(output_path, 'w') as output_file:

    # New headers
    fieldnames = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in formatted:
        writer.writerow({
            fieldnames[0] : row[0], 
            fieldnames[1] : row[1], 
            fieldnames[2] : row[2], 
            fieldnames[3] : row[3], 
            fieldnames[4] : row[4], 
            fieldnames[5] : row[5]
        })
