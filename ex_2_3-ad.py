#! /usr/bin/python3.6

# Get data from kodeData.dat
with open("kodeData.dat", "r") as f:
    kodeData = [line.split() for line in f]

# Get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichend)
itDataStartRow = [lineNumber for lineNumber in range(1, len(kodeData)) if \
len(kodeData[lineNumber]) == int(kodeData[1][0]) and len(kodeData[lineNumber-1]) == int(kodeData[2][0])]


""" --- Exercise 2.3 Advanced --- """

# create empty list for elements of 10x10 iteration blocks
kodeDataSums = [[0 for row in range(10)] for col in range(10)]
xSum = 0

# fill list with summarized values from iteration blocks
for i in range(len(itDataStartRow)):
    xSum += float(kodeData[itDataStartRow[i]-1][0])
    for j in range(10):
        for k in range(10):
            kodeDataSums[j][k] += float(kodeData[itDataStartRow[i]+j][k])
            
# write sums to kodeData-Sums.dat
with open("kodeData-Sums.dat", "w") as f:
    f.write(str(xSum) + "\n")
    f.writelines(line for line in [str(line) + "\n" for line in kodeDataSums])

