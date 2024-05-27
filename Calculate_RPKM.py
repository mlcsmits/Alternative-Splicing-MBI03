import os
import sys
# Functie om RPKM te berekenen
def calculate_RPKM(col2, col3, total_col3):
    return col3 / (col2 / 1000) * (total_col3 / 1000000)

# Loop door alle bestanden in de directory
directory = sys.argv[1]
output_directory = sys.argv[2]

for filename in os.listdir(directory):
    if filename.endswith(".txt"):  # Controleer of het een tekstbestand is
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()[2:]
            total_col3 = sum(float(line.split()[2]) for line in lines)
            
            output_lines = ["Geneid\tLength\tCounts\tRPKM\n"]  # Header toevoegen
            for i, line in enumerate(lines):
                if i < 1:
                    output_lines.append(line)
                else:
                    cols = line.split()
                    col2 = float(cols[1])
                    col3 = float(cols[2])
                    rpkm = calculate_RPKM(col2, col3, total_col3)
                    output_lines.append(f"{line.strip()}\t{rpkm}\n")
            
            # Schrijf de resultaten naar het uitvoerbestand
            output_filename = os.path.join(output_directory, filename)
            with open(output_filename, 'w') as output_file:
                output_file.writelines(output_lines)
