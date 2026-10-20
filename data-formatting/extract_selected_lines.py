#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("Usage: python3 keep_lines.py INPUT_FILE OUTPUT_FILE")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# -----------------------------
# Interactive input for lines to keep
# -----------------------------
print("Enter line numbers/ranges to KEEP (e.g., 1, 3-5, 7, 10-15)")
print("You can enter multiple values separated by commas or spaces")
print("Press Enter on an empty line when finished.")
print("---")

keep_lines = set()

while True:
    try:
        user_input = input("Enter line(s): ").strip()
        if user_input == "":
            break
        
        # Replace commas with spaces and split
        items = user_input.replace(",", " ").split()
        
        for item in items:
            if "-" in item:
                # Range input (e.g., "10-15")
                start, end = map(int, item.split("-"))
                if start > end:
                    start, end = end, start  # Swap if entered backwards
                keep_lines.update(range(start, end + 1))
            else:
                # Single line number
                keep_lines.add(int(item))
        
    except ValueError:
        print("Invalid input. Please enter numbers or ranges (e.g., 5 or 10-15)")
    except KeyboardInterrupt:
        print("\nInput cancelled.")
        sys.exit(1)

# -----------------------------
# Process the file
# -----------------------------
try:
    with open(input_file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)

# Keep only the specified lines (1-based indexing)
filtered = [line for idx, line in enumerate(lines, start=1) if idx in keep_lines]

with open(output_file, "w") as f:
    f.writelines(filtered)

total_lines = len(lines)
kept_count = len(filtered)
deleted_count = total_lines - kept_count

print(f"\nDone!")
print(f"Original lines: {total_lines}")
print(f"Lines kept: {kept_count}")
print(f"Lines deleted: {deleted_count}")
print(f"Output: {output_file}")

if kept_count == 0:
    print("Warning: No lines were kept. Output file will be empty.")
