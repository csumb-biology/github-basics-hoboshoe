#!/usr/bin/env python

#Working template of hydropathy score calculation script
#You need to put in comments for every line
import sys
from matplotlib import pyplot as plt

InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0
winlist=[]
hydlist[]
for i in range(len(sys.argv)):
    if (i==1):
        InSeqFileName=sys.argv[i]
    else:
        window=sys.argv[i]
for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()
InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + ".output.png"
OutFile = open(OutFileName,"w")
lets=0
for win in range(len(ProtSeq)):
    num=0
    lets=sequence[win:win+window]
    if(len(lets)==window):
        for AA in lets:
            num = float(hydrophobicity[AA][1])+num
        hydlist.append(num)
    winlist.append(win)
plt.plot(winlist,hydlist,label='score')
plt.xlabel('Window')
plt.ylabel('Hydropathy Score')
plt.title(%s"'s Hydrophobicity") % (OutFileName)
OutFile.write(OutString + "\n")
OutFile.close()
