#!/usr/bin/env python

import pandas as pd

import matplotlib.pyplot as plt 

import pandas as pd 

cufflinks_output1 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_output3 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_output4 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_output5 = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_output6 = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_output7 = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_output8 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df1 = pd.read_table( cufflinks_output1 )
df2 = pd.read_table( cufflinks_output2 )
df3 = pd.read_table( cufflinks_output3 )
df4 = pd.read_table( cufflinks_output4 )
df5 = pd.read_table( cufflinks_output5 )
df6 = pd.read_table( cufflinks_output6 )
df7 = pd.read_table( cufflinks_output7 )
df8 = pd.read_table( cufflinks_output8 )

all_cuff = [cufflinks_output1, cufflinks_output2, cufflinks_output3, cufflinks_output4, cufflinks_output5, cufflinks_output6, cufflinks_output7, cufflinks_output8]
FPKM = []  

for i in all_cuff:
    f = open (i)
    while True:
        line = f.readline()
        fields = line.rstrip ("\r\n").split("\t") #fields refer to columns, r= the return key, n= the space key, t= tab
        if "Sxl" in line:
            FPKM.append(fields[9])
        if not line:
            break
            
plt.figure()
plt.plot(FPKM)
plt.savefig("FPKM_plot.png") #Unable to get a plot when running the program?

