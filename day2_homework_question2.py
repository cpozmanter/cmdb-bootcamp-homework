#!/usr/bin/env python

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

columns = ["FPKM", "gene_short_name"]

df1, df2, df3, df4, df5, df6, df7, df8.to_csv("Sxl.csv", sep = "\t", index= False)