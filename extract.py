Nr = ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
def extract_columns(input_file, output_file):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        for line in f_input:
            columns = line.strip().split()
            f_output.write('\t'.join(columns[:1] + columns[-2:]) + '\n')
for number in Nr:
    extract_columns(f"/mnt/studentfiles/2024/2024MBI03/Counts/SRR197604{number}_Counts.txt", f"/mnt/studentfiles/2024/2024MBI03/extracted_counts/SRR197604{number}_Counts.txt")
