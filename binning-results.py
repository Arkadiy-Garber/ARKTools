#!/usr/bin/env python3
from collections import defaultdict
import re, os
import textwrap
import argparse


parser = argparse.ArgumentParser(
    prog="fasta-reformat",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    Program for reformatting fasta file alla Anvi'o
    '''))

parser.add_argument('-dir', help='directory of FASTA files')

parser.add_argument('-out', help="output table")

parser.add_argument('-x', help="extension for fasta file")

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


dir = os.listdir(args.dir)
out = open(args.out, "w")
for i in dir:
    if re.findall(args.x, i):
        file = open(args.dir + "/" + i, "r")
        file = fasta(file)
        for j in file.keys():
            out.write(j + "\t" + i + "\n")

