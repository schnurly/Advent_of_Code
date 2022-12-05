index=0
maxCount=0
tmpCount=0
top=[]

import numpy as np

def saveMaxCount():
   global maxCount,tmpCount
   if(tmpCount > maxCount):
      maxCount = tmpCount
   tmpCount = 0

with open('C:\\temp\\aoc_2022\\01_input.txt',"r") as file:
    for line in file:
        if(line == "\n"):
            top.append(tmpCount)
            saveMaxCount()                          
        else:
            tmpCount+=int(line)

saveMaxCount()

a = np.array(top)
ind = np.argpartition(a, -3)[-3:]
top3 = a[ind]
print(sum(top3))
