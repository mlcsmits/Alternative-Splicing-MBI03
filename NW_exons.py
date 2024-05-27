with open("/mnt/studentfiles/2024/2024MBI03/NW_exons.txt", "r") as NW:
    NW_lines = NW.readlines()[1:]
    for line in NW_lines:
        column = line.split('\t')
        if column[1] == 'exon':
            with open("/mnt/studentfiles/2024/2024MBI03/NW_exons_filtered.txt", "a") as filt:
                filt.write(line)