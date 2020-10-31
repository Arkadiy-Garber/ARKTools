#!/usr/bin/env python3
from collections import defaultdict
import re
import os
import textwrap
import argparse
import sys


parser = argparse.ArgumentParser(
    prog="mmseqs-helper.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    *******************************************************
    '''))

parser.add_argument('-b', type=str, help="blast result (13th column must be sname, 14th column must be full_sseq)", default="NA")
parser.add_argument('-o', type=str, help="output fasta file", default="NA")


args = parser.parse_args()


redunDict = defaultdict(list)
file = open(args.b)
out = open(args.o, "w")
for i in file:
    ls = i.rstrip().split("\t")
    if ls[12] not in redunDict.keys():
        out.write(">" + ls[12] + "\n")
        out.write(ls[13] + "\n")
        redunDict[ls[13]].append(ls[1])
        redunDict[ls[12]].append(ls[1])
out.close()




