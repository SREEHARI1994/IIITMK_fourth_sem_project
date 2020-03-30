from Bio.Blast import NCBIWWW
from Bio.SeqIO import parse 


seq_record = next(parse(open('cov2genome.fasta'),'fasta')) 

print(seq_record.seq )

print(len(seq_record.seq ))

result_handle = NCBIWWW.qblast("blastn", "nr", seq_record.seq) 

with open('blast_results4.xml', 'w') as save_file: 
    blast_results = result_handle.read() 
    save_file.write(blast_results)





