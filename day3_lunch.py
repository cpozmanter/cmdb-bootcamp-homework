#!/usr/bin/env python

import sys

seq_name = []  #accumulate data into list
while True:
    line = sys.stdin.readline()
    if line.startswith(">"):
        seq_name.append(line.strip())
    elif line.startswith(">") or line == "":
         break
sequence = "\n".join( seq_name )
print sequence 