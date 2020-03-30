from reportlab.lib import colors 
from reportlab.lib.units import cm 
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO 

record = SeqIO.read("influenza.gb", "genbank")


diagram = GenomeDiagram.Diagram(
   "SARS COV-2") 
track = diagram.new_track(1, name="Annotated Features") 
features = track.new_set()
#print(feature)
print(record.features)
for feature in record.features: 
    if feature.type != "gene": 
       continue 
    if len(feature) % 2 == 0: 
        color = colors.blue 
    else: 
        color = colors.red 
    features.add_feature(feature, color=color, label=True)

diagram.draw(
   format = "linear", orientation = "landscape", pagesize = 'A4', 
   fragments = 4, start = 0, end = len(record)) 
diagram.write("influenza_genome_diagram.png", "PNG")
diagram.write("influenza_genome_diagram.pdf", "PDF")

diagram.draw(
   format = "circular", circular = True, pagesize = (20*cm,20*cm), 
   start = 0, end = len(record), circle_core = 0.7) 
diagram.write("influenza_circular_genome.pdf", "PDF")