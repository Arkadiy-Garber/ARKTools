#!/usr/bin/env python3
# !/bin/sh
# Author: Arkadiy Garber
from collections import defaultdict
import re
import os
import textwrap
import argparse

parser = argparse.ArgumentParser(
    prog="GC-calc",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    Developed by Arkadiy Garber; University of Delaware, Geological Sciences
    Please send comments and inquiries to arkg@udel.edu
    '''))

parser.add_argument('-g', help='genome')

args = parser.parse_args()


def fasta(fasta_file):
    seq = ''
    header = ''
    Dict = defaultdict(lambda: defaultdict(lambda: 'EMPTY'))
    for i in fasta_file:
        i = i.rstrip()
        if re.match(r'^>', i):
            if len(seq) > 0:
                Dict[header] = seq
                header = i[1:]
                seq = ''
            else:
                header = i[1:]
                seq = ''
        else:
            seq += i
    Dict[header] = seq
    return Dict

genome = open(args.g, "r")
genome = fasta(genome)

GC = 0
total = 0
for i in genome.keys():
    seq = genome[i]
    total += len(seq)
    gc = 0
    for bp in seq:
        if bp == "C" or bp == "G":
            GC += 1
            gc += 1
    print(i + "," + str(float(gc/len(seq))))
print("")
print(args.g + "," + str(float(GC/total)))