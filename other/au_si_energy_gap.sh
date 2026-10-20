#!/bin/bash

# Ask for inputs
read -p "Enter first  value (au): " a
read -p "Enter second value (au): " b

# Perform calculation (floating-point safe)
result=$(echo "scale=6; 627.51 * ($a - $b)" | bc)

# Print result
echo
echo "Diff. (kcal/mol) = $result"
echo "================================"
