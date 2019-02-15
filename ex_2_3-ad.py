#! /usr/bin/python3.6

# Get data from kodeData.dat
with open("kodeData.dat", "r") as f:
    kodeData = [line.split() for line in f]

iterBlockLineLength = int(kodeData[1][0])
iterStepLineLength = int(kodeData[2][0])

# Get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichend)
itDataStartRow = [lineNumber for lineNumber in range(1, len(kodeData)) if \
len(kodeData[lineNumber]) == iterBlockLineLength and len(kodeData[lineNumber-1]) == iterStepLineLength]


""" --- Exercise 2.3 Advanced --- """

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
with open("kodeData-Sums.dat", "w") as f:
    f.write(str(xSum) + "\n")
    f.writelines(line for line in [str(line) + "\n" for line in kodeDataSums])

