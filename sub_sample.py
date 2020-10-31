#!/usr/bin/env python3
# !/bin/sh
# Author: Arkadiy Garber
from collections import defaultdict
import statistics
import os
import re
import textwrap
import argparse


parser = argparse.ArgumentParser(
    prog="sub_sample.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    Developed by Arkadiy Garber; University of Delaware, Geological Sciences
    Please send comments and inquiries to arkg@udel.edu
    '''))

parser.add_argument('-fasta', help='input FASTA sequence file')
parser.add_argument('-num_seqs', help="number of sequences you would like to pull out from the fasta file")
parser.add_argument('-output', help="name output file")
args = parser.parse_args()


def fasta(fasta_file):
    out = open(args.output, "w")
    seq = ''
    header = ''
    count = 0
    for i in fasta_file:
        i = i.rstrip()
        if re.match(r'^>', i):
            if count < int(args.num_seqs):
                if len(seq) > 0:
                    out.write(">" + header + "\n")
                    out.write(seq + "\n")
                    count += 1
                    print(count)
                    header = i[1:]
                    seq = ''
                else:
                    header = i[1:]
                    seq = ''
        else:
            seq += i


file = open(args.fasta, "r")
fasta(file)