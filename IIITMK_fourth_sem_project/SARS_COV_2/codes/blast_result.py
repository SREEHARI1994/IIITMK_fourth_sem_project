from Bio.Blast import NCBIXML
from Bio import SearchIO

E_VALUE_THRESH = 1e-20 

blast_qresult = SearchIO.read("blast_results4.xml", "blast-xml")
print(blast_qresult)
first_hsp=blast_qresult[47][0]

print("first",first_hsp)


print("MN996532" in blast_qresult)

for record in NCBIXML.parse(open("blast_results.xml")): 
    if record.alignments:
        print("\n") 
        print("query: %s" % record.query[:100]) 
        for align in record.alignments: 
            for hsp in align.hsps:
                print(hsp.expect) 
                if hsp.expect < E_VALUE_THRESH: 
                    print("match: %s " % align.title[:])