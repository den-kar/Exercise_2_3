#! /usr/bin/python3.6

# Get data from kodeData.dat
with open("kodeData.dat", "r") as f:
    kodeData = [line.split() for line in f]

# Get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichend)
itDataStartRow = [lineNumber for lineNumber in range(1, len(kodeData)) if \
len(kodeData[lineNumber]) == int(kodeData[1][0]) and len(kodeData[lineNumber-1]) == int(kodeData[2][0])]

""" # --- Exercise_2_3 ---

# Write data to "kodeD#.dat" (Format: ". . ."\n, ". . "\n, ...)
for i in range(int(kodeData[1][1])):
    with open("kodeData-1%s.dat" % (i+1), "w") as f:
        f.writelines(line for line in ([" ".join(line) + "\n" for line in kodeData][int(itDataStartRow[i]):(int(itDataStartRow[i])+int(kodeData[1][0]))]))
    print (kodeData[1][0], "iterations saved in kodeD%s.dat" % (i+1), "- step size:", kodeData[itDataStartRow[i]-1])

"""

""" Exercise 2.3 Advanced - Lösungsvariante 1 """
xSum = 0
tempList = [[0 for row in range(10)] for col in range(10)]

for i in range(len(itDataStartRow)):
    xSum += float(kodeData[itDataStartRow[i]-1][0])
    for j in range(10):
        for k in range(10):
            tempList[j][k] += float(kodeData[itDataStartRow[i]+j][k])
            if j == 4 and k == 8:
                print (float(kodeData[itDataStartRow[i]+j][k]))
#            print ("interation: ", i, "- col: ", j, "- row: ", k, ": ", float(kodeData[itDataStartRow[i]+j][k]))
kodeDataSums = [[float(tempList[row][col]) for row in range(10)] for col in range(10)]
#print (kodeDataSums)
print (tempList[4][8]) # Testprint
print (tempList[9][0]) # Testprint

testList = [[[kodeData[itDataStartRow[iteration]+row][col] for iteration in range(len(itDataStartRow))] for row in range(10)] for col in range(10)]
testSum = [[0 for row in range(10)] for col in range(10)]
for i in range(len(itDataStartRow)):
    for j in range(10):
        for k in range(10):
            testSum[j][k] += float(testList[j][k][i])
#print (testSum)
print (testList[0][9]) # Testprint
print (testList[0][9][3]) # Testprint
print (testList[8][4]) # Testprint
print (testList[8][4][2]) # Testprint

with open("kodeData-Sums.dat", "w") as f:
    f.write(str(xSum) + "\n")
    f.writelines(str(line) + "\n" for line in kodeDataSums)

