import subprocess
import sys
import glob

#Usage : python get_SNP_seqs.py contig_positions.txt reference.fasta output.fasta

in_file = sys.argv[1]
reference = sys.argv[2]
out_file = sys.argv[3]

contigs = []

f=open(in_file, 'r')

for i in f:
	loc,cont,pos=i.split(' ')
        start=int(pos)-150
        end=int(pos)+150
        contigs.append(cont+':'+str(start)+'-'+str(end))

#create list of contigs to extract
targets = ' '.join(contigs)

subprocess.call('samtools faidx %s %s > %s' % (reference, targets, out_file), shell=True)

#example: python get_SNP_seqs.py ../bgc/lanes12/beta_outliers_contigs.txt AloPal_combined.a.lines.fasta outliers_beta_300bp.fasta
