#!/usr/bin/python
# this script count otus by phylum from rdp taxonomy assignment
# usage: python count_tax_rdp.py rdp_taxonomy.txt

import sys
import read_rdp_taxonomy
dict = {}
for line in open(sys.argv[1],'r'):
    tax = read_rdp_taxonomy.table(line)
    if dict.has_key(tax[2]):
        temp = dict[tax[2]]
        dict[tax[2]] = temp + 1
    else:
        dict[tax[2]] = 1

for item in dict.items():
    print '\t'.join([item[0],item[1]])
