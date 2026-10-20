#!/bin/bash

# Input file with atom symbols and coordinates (e.g., atoms.xyz)
input_file=$1

# Initialize variables for mass (assumed for common elements) and COM coordinates
total_mass=0
com_x=0
com_y=0
com_z=0

# Atomic masses (in atomic mass units, amu)
declare -A mass
mass=(
  ["H"]=1.008
  ["He"]=4.0026
  ["Li"]=6.94
  ["Be"]=9.0122
  ["B"]=10.81
  ["C"]=12.011
  ["N"]=14.007
  ["O"]=15.999
  ["F"]=18.998
  ["Ne"]=20.180
  ["Na"]=22.990
  ["Mg"]=24.305
  ["Al"]=26.982
  ["Si"]=28.085
  ["P"]=30.974
  ["S"]=32.06
  ["Cl"]=35.45
  ["K"]=39.098
  ["Ar"]=39.948
)

# Read the input file and process each line
while IFS= read -r line
do
  # Parse the atom symbol and coordinates
  symbol=$(echo $line | awk '{print $1}')
  x=$(echo $line | awk '{print $2}')
  y=$(echo $line | awk '{print $3}')
  z=$(echo $line | awk '{print $4}')

  # Get the atomic mass from the dictionary, defaulting to 1 if not found
  atom_mass=${mass[$symbol]:-1}

  # Update the center of mass coordinates
  com_x=$(echo "$com_x + $x * $atom_mass" | bc)
  com_y=$(echo "$com_y + $y * $atom_mass" | bc)
  com_z=$(echo "$com_z + $z * $atom_mass" | bc)

  # Update the total mass
  total_mass=$(echo "$total_mass + $atom_mass" | bc)
done < "$input_file"

# Calculate the final center of mass
com_x=$(echo "$com_x / $total_mass" | bc -l)
com_y=$(echo "$com_y / $total_mass" | bc -l)
com_z=$(echo "$com_z / $total_mass" | bc -l)

# Output the center of mass
echo "Center of Mass: ($com_x, $com_y, $com_z)"

