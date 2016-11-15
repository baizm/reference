import subprocess
import sys

#Usage : python get_SNP_seqs.py contig_positions.txt reference.fasta 250 out.sh

in_file = sys.argv[1]
reference = sys.argv[2]
size = sys.argv[3]
out_sh = sys.argv[4]

contigs = []

f=open(in_file, 'r')
o=open(out_sh, 'w')

for i in f:
	loc,cont,pos=i.split(' ')
        start=int(pos)-int(size)
        end=int(pos)+int(size)
        contigs.append(cont+':'+str(start)+'-'+str(end))

#create list of contigs to extract
targets = ' '.join(contigs)

#write command to file, since subprocess won't work (command is too long, have to run in shell)
o.write('samtools faidx %s %s > all_loci.fasta' % (reference, targets))

#out_sh to be run separately
