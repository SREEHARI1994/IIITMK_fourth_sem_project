from Bio import pairwise2
from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment

file = open("cov2genome.gb") 
records = parse(file, "genbank") 
for record in records:    
   print("Id: %s" % record.id) 
   print("Name: %s" % record.name) 
   print("Description: %s" % record.description) 
   print("Annotations: %s" % record.annotations) 
   print("Sequence Data: %s" % record.seq) 
   print("Sequence Alphabet: %s" % record.seq.alphabet)
   seq1=record.seq
   print(len(record.seq))

file = open("influenza.gb") 
records = parse(file, "genbank") 
for record in records:    
   print("Id: %s" % record.id) 
   print("Name: %s" % record.name) 
   print("Description: %s" % record.description) 
   print("Annotations: %s" % record.annotations) 
   print("Sequence Data: %s" % record.seq) 
   seq2=record.seq
   print("Sequence Alphabet: %s" % record.seq.alphabet)
   print(len(record.seq))

alignments = pairwise2.align.globalxx("ACCGT", "ACG")
print(format_alignment(*alignments[0]))