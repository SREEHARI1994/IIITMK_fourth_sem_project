from Bio.SeqIO import parse 
from Bio.SeqRecord import SeqRecord 
from Bio.Seq import Seq 
from Bio.Data import IUPACData

file = open("cov2genome.fasta") 

records = parse(file, "fasta") 
for record in records:    
   print("Id: %s" % record.id) 
   print("Name: %s" % record.name) 
   print("Description: %s" % record.description) 
   print("Annotations: %s" % record.annotations) 
   print("Sequence Data: %s" % record.seq) 
   print("Sequence Alphabet: %s" % record.seq.alphabet)
   for letter in  IUPACData.ambiguous_dna_letters:
      print(letter,record.seq.count(letter))

   print(len(record.seq))
#displaying genome from genbank file
file = open("cov2genome.gb") 
records = parse(file, "genbank") 
for record in records:    
   print("Id: %s" % record.id) 
   print("Name: %s" % record.name) 
   print("Description: %s" % record.description) 
   print("Annotations: %s" % record.annotations) 
   print("Sequence Data: %s" % record.seq) 
   print("Sequence Alphabet: %s" % record.seq.alphabet)
   for letter in  IUPACData.ambiguous_dna_letters:
      print(letter,record.seq.count(letter))
   print(len(record.seq))
