#!/usr/bin/env python

sam_fname = "/Users/cmdb/data/cmdb-bootcamp-homework/accepted_hits.sam"

f = open( sam_fname ) 
nl = 0
for line in f: 
    if "NH:i:1" in line:
        nl = nl + 1
print nl