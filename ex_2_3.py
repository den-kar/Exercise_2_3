#! /usr/bin/python3.6

with open("kodeData.dat", "r") as f:
    kodeData = [line.split() for line in f] #Get data from kodeData.dat as lists 

iterBlockLength = kodeData[1][0] #count of values in one iteration-block
iterBlocksTotal = kodeData[1][1] #count of iteration-blocks in data
iterBlockStartRow = [i for i in range(1, len(kodeData)) if (len(kodeData[i]) == int(iterBlockLength)\
                                                            and len(kodeData[i-1]) == 1)]
#Get start rows of iteration-blocks (bissi random, aber hinreichende Bedingung)

def writeDataToFileLists(): #write data as lists (Format: "['x','y',...]"\n ['...',...])
    for i in range(int(iterBlocksTotal)):
        with open("kodeZLists%s.dat" % (i+1), "w") as f:
            f.writelines(str(line) + "\n" for line in (kodeData\
                                                       [int(iterBlockStartRow[i]):(int(iterBlockStartRow[i])+10)]))
# + "\n" für Formatierung
writeDataToFileLists()

def writeDataToFileStrings(): #write data as strings (Format: "[x y z ...]"\n [. . ...]) 
    for i in range(int(iterBlocksTotal)):
        with open("kodeZStrings%s.dat" % (i+1), "w") as f:
            f.writelines(line for line in ([" ".join(line) + "\n" for line in kodeData]\
                                           [int(iterBlockStartRow[i]):(int(iterBlockStartRow[i])+10)]))

writeDataToFileStrings()
