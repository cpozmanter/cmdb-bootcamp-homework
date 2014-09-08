#!/usr/bin/env python 

import sys 
import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm
#All work done in terminal will be commented out in this program

#before working with the actual transcripts, decided to write the code I knew how to do, so started by writing the GC content calculator below
# saved sequenced of the transcript.gtf as a .bed, .gtf, and .txt for both positive and negative strands using the following imput in the terminal..
#$ awk '$3 =="transcript"' transcripts.gtf | grep "+" > plus_transcripts.txt
#$ awk '$3 =="transcript"' transcripts.gtf | grep "+" > plus_transcripts.bed
#$ awk '$3 =="transcript"' transcripts.gtf | grep "+" > plus_transcripts.gtf
#$ awk '$3 =="transcript"' transcripts.gtf | grep "-" > minus_transcripts.gtf
#$ awk '$3 =="transcript"' transcripts.gtf | grep "-" > minus_transcripts.txt

# next used bedtools flank, slop, and get fasta programs to retreive the 500bp surrounding the transcription start site.

# $ bedtools flank -l 250 -r 0 -i plus_transcripts.gtf -g /Users/cmdb/data/day3/genome_2col.gff >transcripts_plus.gtf
# $ bedtools slop -l 0 -r 250 -i plus_transcripts.gtf -g /Users/cmdb/data/day3/genome_2col.gff >transcripts_plus_500.gtf
# $ bedtools getfasta -fi /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta -bed transcripts_plus_500.gtf -fo plus_500_sequence.fasta

# $ bedtools flank -l 250 -r 0 -i minus_transcripts.gtf -g /Users/cmdb/data/day3/genome_2col.gff >transcripts_minus.gtf
# $ bedtools slop -l 0 -r 250 -i minus_transcripts.gtf -g /Users/cmdb/data/day3/genome_2col.gff >transcripts_minus_500.gtf
# $ bedtools getfasta -fi /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta -bed transcripts_minus_500.gtf -fo minus_500_sequence.fasta

#The below gc content calculator at first worked perfectly for single lines of sequence. When I tested with two lines or more the output given was 0% GC. I think this is due to white space, thus i added a strip step into my code.


DNA = sys.argv[1].strip("\n\r")

count = 0
for i in range(len(DNA)):
    if DNA[i] == "C" or DNA[i] == "G":
        count = count + 1
    else:
        count = count

gc_total = count

gc_content = float(gc_total) / float(len(DNA))

gc_percent = float(gc_content) * 100.0

print gc_percent

#thought white space bug was fixed with gc content calculator. however when imputing the real sequence file I again got an output of 0.
# tried multiple approuches with no improvement, thus below I wrote code for if I was able to actually do the linear regression. Therefore there is no plot to submit with this program. 

df = pandas.read_csv( "all_fpkms.csv", index_col = 0)

model = sm.formula.ols( formula= "fpkm ~ gc_percent", data=df) #regression left of ~ is dependant variable

res = model.fit()
print res.summary()

plot.scatter( df["fpkm"], df["gc_content"])

plot.savefig("fpkm_vs_gc_content.png")