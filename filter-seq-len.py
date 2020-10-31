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
    prog="filter-seq-len.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    ************************************************************************
    Developed by Arkadiy Garber; University of Montana, Biological Sciences
    Please send comments and inquiries to rkdgarber@gmail.com
    ************************************************************************
    '''))

parser.add_argument('-fasta', help='input FASTA sequence file')
parser.add_argument('-min_len', help="minimum sequence length", default=0)
parser.add_argument('-max_len', help="maximum sequence length", default=20000)
parser.add_argument('-output', help="name output file")
args = parser.parse_args()

file = open(args.fasta, "r")
seq = ''
header = ''
if args.output != args.fasta:
    out = open(args.output, "w")
    for i in file:
        i = i.rstrip()
        if re.match(r'^>', i):
            if len(seq) >= int(args.min_len) and len(seq) <= int(args.max_len):
                print(header)
                out.write(">" + header + "\n")
                out.write(seq + "\n")
                header = i[1:]
                seq = ''
            else:
                header = i[1:]
                seq = ''
        else:
            seq += i

    file.close()
    out.close()
else:
    print("Output file name same as the fasta file. You want your assembly overwritten!?")