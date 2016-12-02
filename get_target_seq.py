import sys
import subprocess

#Usage : python get_target_seq.py reference.fasta contig start stop out.fasta

reference = sys.argv[1]
contig = sys.argv[2]
start = sys.argv[3]
stop = sys.argv[4]
out = sys.argv[5]

o=open(out, 'w')

subprocess.call('samtools faidx %s %s:%s-%s > %s' % (reference, contig, start, stop, out), shell=True)

#used to create a fasta file with sequence extracted from reference genome by calling contig name and position using samtools faidx
