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

def GetEqualSigns(list1,list2,list3):
    retVal = []
    for c in list1:
        if c in list2 and c in list3:
            if c not in retVal:
                retVal.append(c)
    return retVal


prioSum = 0
with open('C:\\temp\\aoc_2022\\03_input.txt',"r") as file:
    lines = []
    for line in file:
        cleanedline = line.strip()
        lines.append(cleanedline)
        if len(lines) == 3:
            for c in GetEqualSigns(lines[0],lines[1],lines[2]):
                prioSum+=chars[c]   
            lines = []
      
            
print(prioSum)
       