#! /usr/bin/python3.6

with open("kodeData.dat", "r") as f:
    kodeDataStrings = [line for line in f]

with open("kodeData.dat", "r") as f:
    kodeDataLists = [(line.split()) for line in f]

nameCounter = 1
for i in range(1, len(kodeDataStrings)):
    if len(kodeDataLists[i]) == 10:
        print ("kodeData Zeile:", str(i), "| Daten aus Iterations-Block %s - Schreibe in kode%s.dat" % (nameCounter,nameCounter))
        with open("kode%s.dat" % (nameCounter), "a") as f:
            f.writelines(kodeDataStrings[i])
    elif len(kodeDataLists[i]) != len(kodeDataLists[i-1]) and len(kodeDataLists[i-1]) == len(kodeDataLists[i-2]):
        print ("kodeData Zeile:", str(i), "|- Ende von Iterations-Block", str(nameCounter), "- in Zeile", str(i-1))
        nameCounter += 1
    else:
        print ("kodeData Zeile:", str(i), "| Inhalt:", kodeDataStrings[i])
