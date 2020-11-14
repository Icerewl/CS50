import sys
import csv
import re

#Opens database and reads it into memory
with open(sys.argv[1], newline='') as f:
    reader = csv.reader(f)
    suspectlist = list(reader)

#Opens sequences and reads it into memory
with open(sys.argv[2], 'r') as f:
    dna = f.readlines()

dnalist = []

#below lines are taking dna's and converts them into strings.
for i in dna:
    as_list = i.split()
    dnalist.append(as_list[0])

strdna = ''.join(dnalist)

#THESE FUNCTIONS ARE CITED FROM STACKOVERFLOW. THEY ARE COUNTING THE LONGEST SEQUENCE OF SRT'S IN DNA
#Specifically cited from Andrej Kesely


patterna = ['AGATC']
m = max([x for p in patterna for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patternb = ['AATG']
n = max([x for p in patternb for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patternc = ['TATC']
o = max([x for p in patternc for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patternd = ['TTTTTTCT']
a = max([x for p in patternd for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patterne = ['TCTAG']
b = max([x for p in patterne for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patternf = ['GATA']
c = max([x for p in patternf for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patterng = ['GAAA']
d = max([x for p in patterng for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))

patternh = ['TCTG']
e = max([x for p in patternh for x in re.findall(r'(({})\2*)'.format(p), strdna)], key=lambda k: len(k[0]) // len(k[1]))


AGATC = len(m[0]) // len(m[1])
AATG = len(n[0]) // len(n[1])
TATC = len(o[0]) // len(o[1])

TTTTTTCT = len(a[0]) // len(a[1])
TCTAG = len(b[0]) // len(b[1])
GATA = len(c[0]) // len(c[1])
GAAA = len(d[0]) // len(d[1])
TCTG = len(e[0]) // len(e[1])

#print(AGATC,AATG,TATC)
#Checks the equality between dna's and srt counts
try:
    if sys.argv[1] == "databases/large.csv":
        for i in range(1,25):

            if int(suspectlist[i][1]) == int(AGATC) and int(suspectlist[i][2]) == int(TTTTTTCT) and int(suspectlist[i][3]) == int(AATG) and int(suspectlist[i][4]) == int(TCTAG) and int(suspectlist[i][5]) == int(GATA) and int(suspectlist[i][6]) == int(TATC) and int(suspectlist[i][7]) == int(GAAA) and int(suspectlist[i][8]) == int(TCTG):
                print(suspectlist[i][0])
                sys.exit(0)

    elif sys.argv[1] == "databases/small.csv":
        for i in range(1,4):

            if int(suspectlist[i][1]) == int(AGATC) and int(suspectlist[i][2]) == int(AATG) and int(suspectlist[i][3]) == int(TATC):
                print(suspectlist[i][0])
                sys.exit(0)
except IndexError:
    print("No match.")
