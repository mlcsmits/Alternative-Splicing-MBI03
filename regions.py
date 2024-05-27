# -*- coding: utf-8 -*-
# Open het bestand 24_1.tsv en bouw een dictionary met geneID als sleutel en de bijbehorende waarden als waarde
geneID_values = {}
path = ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
for value in path:
    with open("/mnt/studentfiles/2024/2024MBI03/RPKM_OLD/NW.tsv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            geneID = columns[4]
            values = columns[:4]
            geneID_values[geneID] = values

# Open het bestand NW.tsv om de geneID's te vergelijken en de overeenkomende waarden te kopiëren
for value in path:
    with open(f"/mnt/studentfiles/2024/2024MBI03/RPKM_calc_SS-WT/SRR197604{value}_Counts_1.tsv", "r") as input_file:
        input_file = input_file.readlines()[1:]
        with open(f"/mnt/studentfiles/2024/2024MBI03/RPKM_calc_SS-WT/{value}.bed", "w") as output_file:
            for line in input_file:
                columns = line.strip().split("\t")
                geneID = columns[0]
                if geneID in geneID_values:
                    values = geneID_values[geneID]
                    output_file.write("\t".join(values) + "\n")
