#!/usr/bin/env python3
from collections import defaultdict
import re
import os
import textwrap
import argparse
import sys


def filter(list, items):
    outLS = []
    for i in list:
        if i not in items:
            outLS.append(i)
    return outLS


def delim(line):
    ls = []
    string = ''
    for i in line:
        if i != " ":
            string += i
        else:
            ls.append(string)
            string = ''
    ls = filter(ls, [""])
    return ls


parser = argparse.ArgumentParser(
    prog="tblout-to-csv.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    *******************************************************

    Developed by Arkadiy Garber and Gustavo Ramírez;
    University of Southern California, Earth Sciences
    Please send comments and inquiries to arkadiyg@usc.edu
    
    Also, please cite: 
    *******************************************************
    '''))

parser.add_argument('-i', type=str, help="input .tblout from hmmsearch result")
parser.add_argument('-o', type=str, help="output csv")



args = parser.parse_args()

out = open(args.o, "w")
tblout = open(args.i)
for i in tblout:
    # if re.findall(r'target', i):
    #     print(delim(i))
    if not re.match('#', i):
        ls = delim(i)
        for j in ls:
            out.write(j + ",")
        out.write("\n")
out.close()