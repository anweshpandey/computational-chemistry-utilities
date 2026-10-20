#!/bin/bash

# Usage: ./kj_kcal input_file output_file

if [ $# -ne 2 ]; then
  echo "Usage: $0 input_file output_file"
  exit 1
fi

input="$1"
output="$2"

awk '
BEGIN { factor = 0.239005736 }

{
  if (index($0, "=") && index($0, "+/-") && index($0, "kJ/mol")) {
    split($0, eq_parts, "=")
    left = eq_parts[1]
    right = eq_parts[2]

    plusminus = index(right, "+/-")
    if (plusminus > 0) {
      val_kj = substr(right, 1, plusminus - 1)
      err_kj = substr(right, plusminus + 3)

      gsub(/[ \t]/, "", val_kj)
      gsub(/[ \t]|kJ\/mol/, "", err_kj)

      val_kcal = val_kj * factor
      err_kcal = err_kj * factor

      printf "%s=     %10.3f   +/-  %7.3f kcal/mol\n", left, val_kcal, err_kcal
      next
    }
  }
  print
}
' "$input" > "$output"

