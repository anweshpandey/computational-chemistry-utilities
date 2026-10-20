#!/bin/bash

echo "==============================================================="
ls -ltr
echo "==============================================================="

# Ask for input
read -p "Enter the name of the ligand .prm file (e.g., ligH.prm): " prm_file
read -p "Enter the name of the ligand .itp file (e.g., ligH.itp): " itp_file
read -p "Enter the name of the ligand position restraint file (e.g., posre_ligH.itp): " posre_file
read -p "Enter the ligand name (e.g., ligH): " ligand_name

# File setup
original="topol.top"
backup="topol_gmx.top"
output="topol.top"

# Backup original
cp "$original" "$backup"

# Process the backup and write final output to topol.top
awk -v prm="$prm_file" -v itp="$itp_file" -v posre="$posre_file" -v name="$ligand_name" '
BEGIN {
    prm_inserted = 0
    inserted_ligand_block = 0
}
{
    # Insert ligand parameter include after forcefield
    if (!prm_inserted && $0 ~ /#include.*forcefield\.itp/) {
        print $0
        print "\n; Include ligand parameters"
        print "#include \"" prm "\""
        prm_inserted = 1
        next
    }

    # When POSRES block ends, insert ligand topology and posre_ligH
    if ($0 ~ /^#endif/ && in_posres_block && !inserted_ligand_block) {
        print $0
        print "\n; Include ligand topology"
        print "#include \"" itp "\""
        print "\n; Ligand position restraints"
        print "#ifdef POSRES_LIG"
        print "#include \"" posre "\""
        print "#endif"
        inserted_ligand_block = 1
        in_posres_block = 0
        next
    }

    if ($0 ~ /#ifdef POSRES/) {
        in_posres_block = 1
    }

    print $0
}
END {
    print name "\t1"
}' "$backup" > "$output"

# Show the diff
echo -e "\n✅ Finished editing. Differences between $backup and $output:"
diff "$backup" "$output"

