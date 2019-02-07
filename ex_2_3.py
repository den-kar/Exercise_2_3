#! /usr/bin/python3.6

#Get data from kodeData.dat
with open("kodeData.dat", "r") as f:
    kodeData = [line.split() for line in f] 

#Get start rows of iteration-blocks (Bedingung bissi random gewählt, aber hinreichende)
iterBlockStartRow = [i for i in range(1, len(kodeData)) if\
                     len(kodeData[i]) == int(kodeData[1][0]) and len(kodeData[i-1]) == int(kodeData[2][0])]

#write data as strings (Format: ". . ."\n, ". . "\n, ...) 
for i in range(int(kodeData[1][1])):
    with open("kodeD%s.dat" % (i+1), "w") as f:
        f.writelines(line for line in ([" ".join(line) + "\n" for line in kodeData]\
                                       [int(iterBlockStartRow[i]):(int(iterBlockStartRow[i])+int(kodeData[1][0]))]))

