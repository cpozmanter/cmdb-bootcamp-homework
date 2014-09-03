#!/usr/bin/env python

sam_fname = "/Users/cmdb/data/cmdb-bootcamp-homework/accepted_hits.sam"

f = open( sam_fname )


for i, line in enumerate( f):
    fields = line.rstrip("\r\n").split("\t")
    if i > 16:
        print fields[2]