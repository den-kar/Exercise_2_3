#!/usr/bin/env python3.6

import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", nargs='?', default="kodeData.dat", help="type source file | default = kodeData.dat")
parser.add_argument("--cut", "-c", action="store_true", help="ONLY cut iteration-blocks and save to seperate files")
parser.add_argument("--sum", "-s", action="store_true", help="ONLY save file with sum of interation-blocks")
args = parser.parse_args()

# get data from file stored in args.file, default = kodeData.dat
with open("{}".format(args.file), "r") as f:
    kodeData = [line.split() for line in f]
# save framing values for iteration-blocks from data sourcefile args.file (default: kodeData.dat) 
nameSubdirectory = kodeData[0][0]
iterBlockLineLength = int(kodeData[1][0])
iterStepLineLength = len(kodeData[2])
numberOfIterBlocks = int(kodeData[1][1])
# get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichend)
itDataStartRow = [lineNumber for lineNumber in range(1, len(kodeData)) if \
len(kodeData[lineNumber]) == iterBlockLineLength and len(kodeData[lineNumber-1]) == iterStepLineLength]


# write each iteration-block to a seperate files SOURCEFILE_iter#.dat
def saveIterationsToFiles():
    for i in range(numberOfIterBlocks):
        with open(os.path.join(os.path.abspath(nameSubdirectory), "{}_iter{}.dat".format(args.file, i+1)), "w") as f:
            f.writelines(line for line in (\
    [" ".join(line) + "\n" for line in kodeData][int(itDataStartRow[i]):(int(itDataStartRow[i])+iterBlockLineLength)]))

# write sum of iterations to SOURCEFILE_sums.dat
def saveIterationsSums():
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
    with open(os.path.join(os.path.abspath(nameSubdirectory), "{}_sums.dat".format(args.file)), "w") as f:
        f.write(str(xSum) + "\n")
        f.writelines(line for line in [str(line) + "\n" for line in kodeDataSums])

# check if subdirectory exists, create if it doens't
def checkDirExist():
    try:
        os.mkdir(nameSubdirectory)
    except Exception:
        pass
        
def main(cut, sum):
    checkDirExist()
    if cut == False and sum == False:
        saveIterationsToFiles()    
        saveIterationsSums()
    elif cut == True:
        saveIterationsToFiles()
    elif sum == True:
        saveIterationsSums()

main(args.cut, args.sum)

