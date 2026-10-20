#!/bin/bash

input_file="$1"
output_file="$2"

# Ask the user for the maximum value of 'i'
read -p "Enter the maximum value for i: " max_i

# Validate input to ensure it's a positive integer
if ! [[ "$max_i" =~ ^[0-9]+$ ]] || [ "$max_i" -le 0 ]; then
    echo "Error: Please enter a positive integer."
    exit 1
fi

# Ask the user for the maximum value of 'j'
read -p "Enter the maximum value for j: " max_j

# Validate input to ensure it's a positive integer
if ! [[ "$max_j" =~ ^[0-9]+$ ]] || [ "$max_j" -le 0 ]; then
    echo "Error: Please enter a positive integer."
    exit 1
fi

# Read number of basis functions and number of orbitals
read -r number_bf num_orb < "$input_file"

# Initialize an associative array to store the data
declare -A a

i=1
j=1
while read -r line && [ "$j" -le "$max_j" ]; do
    for value in $line; do
        a[$i,$j]="$value"
        ((i++))
    done
    if [ "$i" -gt "$max_i" ]; then
        i=1
        ((j++))
    fi
done < <(tail -n +2 "$input_file")

# Write formatted data to the output file
{
    for ((k=1; k<=10; k++)); do
        j=$((5 * k - 4))
        for ((i=1; i<=max_i; i++)); do
            printf "%10.5f%10.5f%10.5f%10.5f%10.5f\n" \
                "${a[$i,$j]}" "${a[$i,$((j+1))]}" "${a[$i,$((j+2))]}" \
                "${a[$i,$((j+3))]}" "${a[$i,$((j+4))]}"
        done
        echo
    done
} > "$output_file"

echo "Output saved to $output_file."

