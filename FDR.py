import sys
import os
AS = ['SE', 'MXE', 'RI', 'A3SS', 'A5SS']
directory1 = sys.argv[1]
directory2 = sys.argv[2]
os.mkdir(directory2)
for i in AS:
    # Pad naar het oorspronkelijke bestand
    input_file_path = f"{directory1}{i}.MATS.JCEC.txt"
    # Pad naar het nieuwe bestand
    output_file_path = f"{directory2}{i}.MATS.JCEC.txt"

    # Open het oorspronkelijke bestand in leesmodus
    output_file_header = "ID\tGeneID\tgeneSymbol\tchr\tstrand\texonStart_0base\texonEnd\tupstreamES\tupstreamEE\tdownstreamES\tdownstreamEE\tID\tIJC_SAMPLE_1\tSJC_SAMPLE_1\tIJC_SAMPLE_2\tSJC_SAMPLE_2\tIncFormLen\tSkipFormLen\tPValue\tFDR\tIncLevel1\tIncLevel2\tIncLevelDifference\n"
    with open(input_file_path, 'r') as input_file:
        # Open het nieuwe bestand in schrijfmodus
        with open(output_file_path, 'w') as output_file:
            output_file.write(output_file_header)
            next(input_file)
            # Loop door elke regel in het oorspronkelijke bestand
            for line in input_file:
                # Split de regel op tab-tekens
                parts = line.strip().split('\t')
                # Controleer of de waarde in de kolom FDR lager is dan 0.05
                if len(parts) > 0 and float(parts[19]) < 0.05:
                    # Schrijf de hele regel naar het nieuwe bestand
                    output_file.write(line)
