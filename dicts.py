#print a dict

edadDict = { 'victor':45, 'diego':17, 'viso':18 }
print (edadDict)

suma = 0
for item in edadDict:
    print ( item, 'tiene', edadDict[item], sep=' ', end='\n')