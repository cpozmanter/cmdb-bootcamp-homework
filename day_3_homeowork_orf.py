#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""
import sys

from fasta import FASTAReader 
        
reader = FASTAReader( sys.stdin )        

seq_length = []
actual_sequence = []
list_of_duples = []
for sid, sequence in reader:
    seq_length.append(len(str(sequence)))
    actual_sequence.append(str(sequence))
    list_of_duples = zip(seq_length, actual_sequence)
    print list_of_duples
sort_list = sorted(list_of_duples[0], reverse=True)

transcripts = sort_list[0:100]


#how to export to fasta format, and deal with the number there representing the length of the sequence?
#how to make reverse complememt?
#in mean time work on how to find and translate orf 
#code below is a variation and mix of multiple approaches found on google
# helpful website to refer to: https://github.com/mtarbit/Rosalind-Problems/blob/master/e017-orf.py, 


start_codon = "ATG"  #will need to tell program what a start codon is
stop_codons = ["TAG", "TGA", "TAA"] #and what a stop codon is

#do i need to define stop and start seperate from the condon table?

codon_table = {"GCT" : "A", "GCC" : "A","GCA" : "A", "GCG" : "A", "TGT" : "C", "TGC" : "C", "GAT" : "D", "GAC" : "D", 
               "GAA" : "E", "GAG" : "E", "TTT" : "F", "TTC" : "F", "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G",
               "CAT" : "H", "ATT" : "I", "ATC" : "I","ATA" : "I", "CAC" : "H", "AAA" : "K", "AAG" : "K", "TTA" : "L", 
               "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "ATG" : "M",  "AAT" : "N", "AAC" : "N",
               "CCT" : "P", "CCC" : "P",  "CCA" : "P", "CCG" : "P", "CAA" : "Q", "CAG" : "Q", "CGT" : "R", "CGC" : "R", 
               "CGA" : "R", "CGG" : "R", "AGA" : "R","AGG" : "R", "TCT" : "S", "TCC" : "S", "TCA" : "S","TCG" : "S", 
               "AGT" : "S", "AGC" : "S", "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "GTT" : "V", "GTC" : "V", 
               "GTA" : "V","GTG" : "V","TGG" : "W", "TAT" : "Y", "TAC" : "Y", "TAA" : "stop", "TAG" : "stop", "TGA" : "stop"}
                #dicitonary of codons for future translation
#how/where to define codon?
def protein_seq(s):
    results = []
    indices = []

def translate_codon(transcripts): #how to send the 100 sequences to the translator?
    protein = None
    if len(codon) == 3 and codon_table.has_key(codon):
        protein = codon_table[codon]
    return protein

l = len(s)
for i in range(l):
    protein = translate_codon(s[i:i+3])
    if protein == "M":
        indices.append(i)

for b in range(i, l, 3):  #called b to remind me of DNA base
    protein = translate_codon(s[j:j+3])
    if not protein:
        break
    if protein == "Stop":
        stop = True
        break

protein_seq += protein

if found_stop:
    results.append(protein_seq)
print results #results is list of translated transcripts 

   
   #make empty list as place holder something = [] 
   #for sid, sequence in reader:
       #something.append
        # len()  , str()
        # goal here is to make a list full of each sequence's length

#highlight and then command right bracket indents everything that was highlighted

#print is it ok
# figure out how to use sorted()