f = open('promote.in', 'r')
line = f.readline()
startingBronze = int(line.split()[0])
endingBronze = int(line.split()[1])
line = f.readline()
startingSilver = int(line.split()[0])
endingSilver = int(line.split()[1])
line = f.readline()
startingGold = int(line.split()[0])
endingGold = int(line.split()[1])
line = f.readline()
startingPlat = int(line.split()[0])
endingPlat = int(line.split()[1])
f.close()
bronzeToSilver = (endingPlat-startingPlat)+(endingGold-startingGold)+(endingSilver-startingSilver)

silverToGold = (endingGold-startingGold) + (endingPlat-startingPlat)

goldToPlat = endingPlat - startingPlat;

f = open('promote.out', 'w')
f.write((str(bronzeToSilver))+ '\n')
f.write((str(silverToGold))+ '\n')
f.write((str(goldToPlat)) + '\n')
f.close()



