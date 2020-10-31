#!/usr/bin/env python3
# !/bin/sh
from collections import defaultdict
import re
import os
import textwrap
import argparse
import urllib.request
import ssl

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


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

parser = argparse.ArgumentParser(
    prog="seq-check.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    *******************************************************
    Developed by Arkadiy Garber; 
    University of Delaware, Geological Sciences
    Please send comments and inquiries to arkg@udel.edu
    *******************************************************
    '''))

parser.add_argument('-in', type=str, help='fasta file in which you would like to get rid of empty sequences and associated headers')

parser.add_argument('-out', type=str, help="output fasta")

args = parser.parse_args()


file = open(args.on, "r")
out = open(args.out, "w")
file = fasta(file)
for j in file.keys():
    if len(file[j]) != 0:
        out.write(">" + j + "\n")
        out.write(file[j] + "\n")