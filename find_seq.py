import sys
import gzip
from Bio import SeqIO

query = sys.argv[2].lower()
ref = gzip.open(sys.argv[1], 'r')

for record in SeqIO.parse(ref,'fasta'):
    indeces = []
    i = str(record.seq).lower().find(query)
    while i >= 0:
        indeces.append(str(i + 1))
        i =  str(record.seq).lower().find(query, i + 1)

    if len(indeces) > 0:
        print record.id + "\t" + ','.join(indeces)

ref.close()

#usage: python find_seq.py AloPal_combined.a.lines.fasta.gz 'ATTACAG'
