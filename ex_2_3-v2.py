#! /usr/bin/python3.6

with open("kodeData.dat", "r") as f:
    kodeDataStrings = [line for line in f]

with open("kodeData.dat", "r") as f:
    kodeDataLists = [(line.split(" ")) for line in f]

nameCounter = 1
for i in range(1, len(kodeDataStrings)):
    if len(kodeDataLists[i]) == 10:
        print ("Daten aus Iterations-Block; kodeData Zeile:", str(i), "- Schreibe in \"kode-test%s.dat" % (nameCounter))
        with open("kode%s.dat" % (nameCounter), "a") as f:
            f.writelines(kodeDataStrings[i])
    elif len(kodeDataLists[i][0]) != len(kodeDataLists[i-1][0]) and len(kodeDataLists[i-1][0]) == len(kodeDataLists[i-2][0]):
        print ("Ende Iterations-Block %s; kodeData Zeile:" % (nameCounter), str(i))
        nameCounter += 1
    else:
        print ("nix los hier, Zeile:", str(i), "- Inhalt:", kodeDataStrings[i])
