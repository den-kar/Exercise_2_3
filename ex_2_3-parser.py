#!/usr/bin/env python3.6

import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", nargs='?', default="kodeData.dat", help="mandatory input: type source file")
parser.add_argument("--split", "-sp", action="store_true", help="get split files for iterations only")
parser.add_argument("--sums", "-sum", action="store_true", help="get sum file of iterations only")
args = parser.parse_args()

# get data from file stored in args.file, default = kodeData.dat
with open("{}".format(args.file), "r") as f:
    kodeData = [line.split() for line in f]
# save frame values from data source
nameSubdirectory = kodeData[0][0]
iterBlockLineLength = int(kodeData[1][0])
iterStepLineLength = len(kodeData[2])
numberOfIterBlocks = int(kodeData[1][1])
# get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichend)
itDataStartRow = [lineNumber for lineNumber in range(1, len(kodeData)) if \
len(kodeData[lineNumber]) == iterBlockLineLength and len(kodeData[lineNumber-1]) == iterStepLineLength]


def saveIterationsToFiles():
# check if subdirectory exists, create if it doens't
    try:
        os.mkdir(nameSubdirectory)
    except Exception:
        pass
# write data to "kodeD#.dat" (Format: ". . ."\n, ". . "\n, ...)
    for i in range(numberOfIterBlocks):
        with open(os.path.join(os.path.abspath(nameSubdirectory), "kodeD{}.dat".format(i+1)), "w") as f:
            f.writelines(line for line in (\
    [" ".join(line) + "\n" for line in kodeData][int(itDataStartRow[i]):(int(itDataStartRow[i])+iterBlockLineLength)]))
"""        print ("{} iterations saved in kodeD{}.dat - step size: {}".format(iterBlockLineLength, i+1, kodeData[itDataStartRow[i]-1]))
"""
def saveIterationsSums():
# check if subdirectory exists, create if it doens't
    try:
        os.mkdir(nameSubdirectory)
    except Exception:
        pass
# invoke empty list for elements of 10x10 iteration blocks
    kodeDataSums = [[0 for row in range(iterBlockLineLength)] for col in range(iterBlockLineLength)]
    xSum = 0
# fill list with summarized values from iteration blocks
    for i in range(len(itDataStartRow)):
        xSum += float(kodeData[itDataStartRow[i]-1][0])
        for j in range(iterBlockLineLength):
            for k in range(iterBlockLineLength):
                kodeDataSums[j][k] += float(kodeData[itDataStartRow[i]+j][k])
# write sums to kodeData-Sums.dat
    with open(os.path.join(os.path.abspath(nameSubdirectory), "kodeData-Sums.dat"), "w") as f:
        f.write(str(xSum) + "\n")
        f.writelines(line for line in [str(line) + "\n" for line in kodeDataSums])
        
def main(split, sums):
    if split == False and sums == False:
        saveIterationsToFiles()    
        saveIterationsSums()
    elif split == True:
        saveIterationsToFiles()
    elif sums == True:
        saveIterationsSums()

main(args.split, args.sums)