#!/usr/bin/env python3
# !/bin/sh
# Author: Arkadiy Garber

from collections import defaultdict
import re
import os
import textwrap
import argparse

parser = argparse.ArgumentParser(
    prog="seq-len",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    ************************************************************************
    ************************************************************************
    Developed by Arkadiy Garber; University of Delaware, Geological Sciences
    Please send comments and inquiries to arkg@udel.edu
    ************************************************************************
    ************************************************************************
    '''))


parser.add_argument('-fasta', help='fasta file')

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


file = open(args.fasta, "r")
file = fasta(file)
ls = []
for i in file.keys():
    ls.append(len(file[i]))

count = 1
for i in sorted(ls, reverse=True):
    print(str(count) + ": " + str(i))
    count += 1
