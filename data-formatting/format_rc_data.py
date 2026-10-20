#!/usr/bin/env python3

def get_data():
    # Prompt user for the data input
    print("Please enter your data (press Enter twice to finish):")
    data = []
    while True:
        line = input()
        if line == "":
            break
        data.append(line.strip())
    return data

# Get the data from the user
data = get_data()

# Split the data into rows and then into columns
column_data = []
for row in data:
    # Split each row into columns and add to the list
    column_data.extend(row.split())

# Write the column data to output
for item in column_data:
    print(item)

