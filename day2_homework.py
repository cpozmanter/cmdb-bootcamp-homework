#!/usr/bin/env python

import pandas as pd 

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"

df = pd.read_table( cufflinks_output )

import matplotlib.pyplot as plt 

cufflinks_output2= "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df2 = pd.read_table( cufflinks_output2 )

#fm = open( cufflinks_output)
#ff = open( cufflinks_output2)

#nlm =0
#while True:
   # line = fm.readline()
    #if line == "":
     #   break
    #else:
     #   nlm = nlm + 1

#nlf = 0
#while True:
 #   line = ff.readline()
  #  if line == "":
   #     break
    #else:
     #   nlf = nlf + 1

#a = nlm/3
#b = 2*nlm


#d = nlf/3
#e = 2* nlf


#males = df.sort("FPKM", ascending = False)
#females = df2.sort("FPKM", ascending = False)

males_1 = df.sort("FPKM")[0:5200]
males_2 = df.sort("FPKM")[5201:10401]
males_3 = df.sort("FPKM")[10402:15602]

females_1 = df2.sort("FPKM")[0:5200]
females_2 = df2.sort("FPKM")[5201:10401]
females_3 = df2.sort("FPKM")[10402:15602]

#master_list = []
#for i in males_1, males_2, males_3, females_1, females_2, females_3: 
        #master_list.append(i)

master_list = [males_1, males_2, males_3, females_1, females_2, females_3]

plt.figure()

plt.boxplot(master_list)
plt.savefig("boxplot.png")


