#!/bin/bash

# Check if input file is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file="$1"

# Initialize sums
sum_Z=0
sum_X=0
sum_Y=0
sum_Z_coord=0

# Read the file line by line
while read -r Z x y z; do
    sum_Z=$((sum_Z + Z))
    sum_X=$(echo "$sum_X + $Z * $x" | bc -l)
    sum_Y=$(echo "$sum_Y + $Z * $y" | bc -l)
    sum_Z_coord=$(echo "$sum_Z_coord + $Z * $z" | bc -l)
done < "$input_file"

# Compute CNC coordinates
CNC_X=$(echo "$sum_X / $sum_Z" | bc -l)
CNC_Y=$(echo "$sum_Y / $sum_Z" | bc -l)
CNC_Z=$(echo "$sum_Z_coord / $sum_Z" | bc -l)

# Output the result
echo "Center of Nuclear Charge (CNC):"
echo "X = $CNC_X"
echo "Y = $CNC_Y"
echo "Z = $CNC_Z"

