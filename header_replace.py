#!/usr/bin/env python3
import argparse
import os
import re
from collections import defaultdict

parser = argparse.ArgumentParser(description='Program for replacing headers')
parser.add_argument('in_filename', help='In fasta file')
parser.add_argument('out_directory', help='Directory')
args = parser.parse_args()

with open(args.in_filename) as fastaFile:
    def replace(stringOrlist, list, string):
        emptyList = []
        for i in stringOrlist:
            if i not in list:
                emptyList.append(i)
            else:
                emptyList.append(string)
        outString = "".join(emptyList)
        return outString


    def fix(stringOrlist, string):
        emptyList = []
        for i in stringOrlist:
            if re.match(r'\w', i):
                emptyList.append(i)
            else:
                emptyList.append(string)
        outString = "".join(emptyList)
        return outString


    def fasta(fasta_file):
        illegalCharacters = [":", ",", "(", ")", ";", "[", "]", "'", " ", "|", "#"]
        seq = ''
        header = ''
        Dict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
        for i in fasta_file:
            i = i.rstrip()
            if re.match(r'^>', i):
                if len(seq) > 0:
                    Dict[header] = seq
                    header = fix(i[1:], "_")
                    seq = ''
                else:
                    header = fix(i[1:], "_")
                    seq = ''
            else:
                seq += i
        Dict[header] = seq
        return Dict
    outfile = open("%s/%s_fixed.fa" % (args.out_directory, args.in_filename), 'w')
    fa = fasta(fastaFile)
    for i in fa.keys():
        outfile.write(">" + i + "\n")
        outfile.write(fa[i] + "\n")