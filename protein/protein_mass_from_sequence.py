#!/usr/bin/env python3
"""
Protein Mass Calculator
Calculates the molecular mass of a protein sequence in Daltons (Da)
"""

def calculate_protein_mass(sequence):
    """
    Calculate the molecular mass of a protein sequence in Daltons.
    
    Args:
        sequence (str): Single-letter amino acid sequence
        
    Returns:
        float: Molecular mass in Daltons
    """
    
    # Molecular weights of amino acid residues (in Daltons)
    # These are the average molecular weights after removal of water during peptide bond formation
    # 
    # REFERENCES:
    # 1. IUPAC-IUB Commission on Biochemical Nomenclature (1985)
    #    "Nomenclature and Symbolism for Amino Acids and Peptides"
    #    Eur. J. Biochem. 138, 9-37
    #
    # 2. Fasman, G.D. (1989) "Practical Handbook of Biochemistry and Molecular Biology"
    #    CRC Press, Boca Raton, FL
    #
    # 3. NIST Atomic Masses and Isotopic Compositions Database
    #    https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions
    #
    # 4. ExPASy - ProtParam tool reference values
    #    https://web.expasy.org/protparam/
    #    Gasteiger E., Hoogland C., Gattiker A., Duvaud S., Wilkins M.R., Appel R.D., Bairoch A.
    #    "Protein Identification and Analysis Tools on the ExPASy Server"
    #    In: John M. Walker (ed): The Proteomics Protocols Handbook, Humana Press (2005) pp. 571-607
    #
    # 5. Handbook of Chemistry and Physics, CRC Press (current edition)
    #
    # Values calculated as: Molecular weight of amino acid - H2O (18.01528 Da)
    aa_weights = {
        'A': 71.0788,   # Alanine (C3H7NO2 - H2O = 89.0935 - 18.0153 = 71.0782)
        'R': 156.1875,  # Arginine (C6H14N4O2 - H2O = 174.2017 - 18.0142 = 156.1875)
        'N': 114.1038,  # Asparagine (C4H8N2O3 - H2O = 132.1184 - 18.0146 = 114.1038)
        'D': 115.0886,  # Aspartic acid (C4H7NO4 - H2O = 133.1032 - 18.0146 = 115.0886)
        'C': 103.1388,  # Cysteine (C3H7NOS - H2O = 121.1590 - 18.0202 = 103.1388)
        'E': 129.1155,  # Glutamic acid (C5H9NO4 - H2O = 147.1299 - 18.0144 = 129.1155)
        'Q': 128.1307,  # Glutamine (C5H10N2O3 - H2O = 146.1451 - 18.0144 = 128.1307)
        'G': 57.0519,   # Glycine (C2H5NO2 - H2O = 75.0669 - 18.0150 = 57.0519)
        'H': 137.1411,  # Histidine (C6H9N3O2 - H2O = 155.1552 - 18.0141 = 137.1411)
        'I': 113.1594,  # Isoleucine (C6H13NO2 - H2O = 131.1736 - 18.0142 = 113.1594)
        'L': 113.1594,  # Leucine (C6H13NO2 - H2O = 131.1736 - 18.0142 = 113.1594)
        'K': 128.1741,  # Lysine (C6H14N2O2 - H2O = 146.1882 - 18.0141 = 128.1741)
        'M': 131.1926,  # Methionine (C5H11NOS - H2O = 149.2124 - 18.0198 = 131.1926)
        'F': 147.1766,  # Phenylalanine (C9H11NO2 - H2O = 165.1891 - 18.0125 = 147.1766)
        'P': 97.1167,   # Proline (C5H9NO2 - H2O = 115.1310 - 18.0143 = 97.1167)
        'S': 87.0782,   # Serine (C3H7NO3 - H2O = 105.0930 - 18.0148 = 87.0782)
        'T': 101.1051,  # Threonine (C4H9NO3 - H2O = 119.1197 - 18.0146 = 101.1051)
        'W': 186.2132,  # Tryptophan (C11H12N2O2 - H2O = 204.2252 - 18.0120 = 186.2132)
        'Y': 163.1760,  # Tyrosine (C9H11NO3 - H2O = 181.1894 - 18.0134 = 163.1760)
        'V': 99.1326    # Valine (C5H11NO2 - H2O = 117.1469 - 18.0143 = 99.1326)
    }
    
    # Convert to uppercase and remove whitespace
    sequence = sequence.upper().strip()
    
    # Validate sequence
    invalid_chars = []
    for char in sequence:
        if char not in aa_weights:
            invalid_chars.append(char)
    
    if invalid_chars:
        raise ValueError(f"Invalid amino acid characters found: {set(invalid_chars)}")
    
    # Calculate mass of all amino acid residues
    total_mass = sum(aa_weights[aa] for aa in sequence)
    
    # Add mass of water (H2O = 18.01528 Da) to get the mass of the intact protein
    # This accounts for the N-terminus (H) and C-terminus (OH)
    water_mass = 18.01528
    protein_mass = total_mass + water_mass
    
    return protein_mass


def main():
    """Main function to get user input and calculate protein mass."""
    
    print("Protein Mass Calculator")
    print("=" * 50)
    print("Enter a protein sequence using single-letter amino acid codes.")
    #print("Valid amino acids: A, R, N, D, C, E, Q, G, H, I, L, K, M, F, P, S, T, W, Y, V")
    print("Press Ctrl+C to exit at any time.")
    print()
    
    while True:
        try:
            # Get protein sequence from user
            sequence = input("Enter protein sequence: ").strip()
            
            # Allow user to exit by typing 'n'
            if sequence.lower() == 'x':
                break
            
            # Check if sequence is empty
            if not sequence:
                print("Please enter a valid sequence (or 'x' to exit).")
                continue
                
            # Calculate mass
            mass = calculate_protein_mass(sequence)
            
            # Display results
            print(f"\nResults:")
            #print(f"Sequence: {sequence}")
            print(f"Length: {len(sequence)} amino acids")
            print(f"Molecular mass (Da): {mass:.4f} Da")
            print(f"Molecular mass (kDa): {mass/1000:.4f} kDa")
            print("=" * 50)  # Add separator line
                
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid protein sequence (or 'n' to exit).")
            print("*" * 50)  # Add separator line after error too
            continue
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
    
    print("Thank you for using the Protein Mass Calculator!")


if __name__ == "__main__":
    main()
