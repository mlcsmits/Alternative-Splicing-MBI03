# Alternative-Splicing-MBI03
Github repository of the project "Prediction of alternative splicing at insecticide resistance genes in Culex quinquefasciatus" by Michel Smits and Milan Vissers - Avans University of Applied Sciences

![image](https://github.com/mlcsmits/Alternative-Splicing-MBI03/assets/161313142/5b902179-006a-4f4c-9d7a-db445e74135b)


# Importing, Trimming, Quality Control, Mapping and featurecounting
To import the fastq files from the SRA run the pipeline.sh file with the command:

bash pipeline.sh

# Preprocessing for rMATS
To filter the regions out of the mapped bam files run the following python scripts

Nr=(17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36)

python3 ~/extract.py

python3 ~/Calculate_RPKM.py /path/to/extracted_counts/ /path/to/RPKM_calc/dir/

To filter the genes with RPKM > 1 from the rest run this code:

python3 ~/RPKM.py

python3 ~/regions.py

bedtools intersect -abam ~/sorted/sorted_SRR197604${Nr[i]}.bam -b ~/RPKM/${Nr[i]}.bed > ~/sorted/subset_SRR197604${Nr[i]}.bam

# Running rMATS
Install rMATS using this link
[https://github.com/Xinglab/rmats-turbo.git](https://github.com/Xinglab/rmats-turbo/tree/v4.2.0)

To run the alternative splicing prediction, use rMATS, fill in the --b1 and --b2 depending on which samples you want to compare.

python3 ~/rmats_turbo_v4_2_0/rmats.py --b1 ~/MS_or_SS.txt --b2 ~/MR_or_WT.txt --gtf ~/RefSeq/genomic.gtf -t paired --readLength 100 --nthread 5 --od ~/rmats_output/ --tmp ~/rmats_output/

# Filter the significant reads
To filter the significant reads with FDR<0.05 run this code:

python3 ~/FDR.py ~/path/to/rmats_out/ ~/path/to/rmats_out_2/

# Run rmats2sashimiplot
Install rmats2sashimiplot using this link
https://github.com/Xinglab/rmats2sashimiplot/tree/kutscherae-output-coords

To visualise the sashimiplots of the exon skipping events from rMATS, run rmats2sashimiplot with the modified script for making coordinate files, fill in the --b1, --b2, --l1, and --l2 depending on which samples you want to compare.

python3 rmats2sashimiplot-master/src/rmats2sashimiplot/rmats2sashimiplot.py --b1 ~/MS_or_SS.txt --b2 ~/MR_or_WT.txt -c ~/RefSeq/genomic.gff3 --group-info ~/group_M.gf --event-type SE -e ~/rmats_out_2/SE.MATS.JCEC.txt --l1 MS_or_SS --l2 MR_or_WT -o ~/plot_SE_out --intron_s 5

To count all the junctions in GST1-6 use the following rmats2sashimiplot script, fill in the --b1, --b2, --l1, and --l2 depending on which samples you want to compare.

python3 rmats2sashimiplot-master/src/rmats2sashimiplot/rmats2sashimiplot.py --b1 ~/MS_or_SS.txt --b2 ~/MR_or_WT.txt --group-info ~/group_M.gf -c NW_001886736.1:+:73175:79227:/mnt/studentfiles/2024/2024MBI03/RefSeq/genomic.gff3 --l1 MS_or_SS --l2 MR_or_WT -o plot_JUNCTIONS --intron_s 5


To give the coordinate files the same number as the pdf files of the sashimi plots run ReplaceNamesCoords.py

python3 ~/ReplaceNamesCoords.py /path/to/Sashimi_plot/dir
