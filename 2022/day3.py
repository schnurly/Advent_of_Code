from string import ascii_lowercase
from string import ascii_uppercase

chars = {}

index=1
for c in ascii_lowercase:
    chars[c]=index
    index+=1
for c in ascii_uppercase:
    chars[c]=index
    index+=1

def GetEqualSigns(list1,list2):
    retVal = []
    for c in list1:
        if c in list2:
            if c not in retVal:
                retVal.append(c)
    return retVal


prioSum = 0
with open('C:\\temp\\aoc_2022\\03_input.txt',"r") as file:
    for line in file:
        cleanedline = line.strip()
        splitLength = int(len(cleanedline)/2)
        left = cleanedline[:splitLength]
        right = cleanedline[-splitLength:]
        for c in GetEqualSigns(left,right):
            prioSum+=chars[c]              
print(prioSum)
       