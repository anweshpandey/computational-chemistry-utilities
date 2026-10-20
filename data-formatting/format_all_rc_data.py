#!/usr/bin/env python3

def read_file_in_columns(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        data = file.readlines()
    
    # Process data in chunks of 32 lines
    columns = []
    for i in range(0, len(data), 32):
        chunk = data[i:i+32]
        column_data = []
        for line in chunk:
            # Split each line into columns and append them to the list
            column_data.extend(line.split())
        columns.append(column_data)

    # Now print the columns
    max_len = max(len(column) for column in columns)  # Find the longest column
    for row_idx in range(max_len):
        for col in columns:
            # Print the corresponding row from each column, rounded to 5 decimal places
            if row_idx < len(col):
                try:
                    print(f"{float(col[row_idx]):.5f}", end=" ")
                except ValueError:
                    print(col[row_idx], end=" ")  # In case the value is not a number
            else:
                print(" ", end=" ")
        print()  # Move to the next line

# Replace with your actual input filename
filename = 'nbo.txt'  # Example input file

read_file_in_columns(filename)

