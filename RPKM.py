def process_tsv(input_file):
    output_file = input_file.replace('.txt', '_1.tsv')

    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        next(f_input)  # Skip the first line
        f_output.write("geneID\n")  # Write the header to the new file
        for line in f_input:
            columns = line.strip().split('\t')
            last_column_value = float(columns[-1])  # Assuming the last column contains numeric values
            if last_column_value > 1:
                f_output.write(columns[0] + '\n')  # Write the value from the first column to the new file

path = ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
for value in path:
    process_tsv(f"/mnt/studentfiles/2024/2024MBI03/RPKM_calc/SRR197604{value}_Counts.txt")
    print("Proces voltooid.")
