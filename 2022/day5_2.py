
stack = {}
preStack = []
preInstruction = []
isInstructionInput=False
with open('C:\\temp\\aoc_2022\\05_input.txt',"r") as file:
    for line in file:
        linecleaned = line.replace('\n','')
    
        if(linecleaned == ""):
            isInstructionInput=True
            continue
        if(isInstructionInput):
            preInstruction.append(linecleaned)
        else:
            preStack.append(linecleaned)


for index in range(len(preStack)-1,-1,-1):
    if(index == len(preStack)-1):
        for pos in range(0,len(preStack[index])):
            if(preStack[index][pos] != " "):
                if(preStack[index][pos] not in stack):
                    stack[preStack[index][pos]] = []
            
    else:
        stackPos = 1
        for pos in range(0,len(preStack[index])):            
            if(pos % 4 == 1):
              if preStack[index][pos] != " ":
                stack[str(stackPos)].append(preStack[index][pos])
              stackPos+=1

for line in stack:
    print(stack[line])


import re
instructionCount=0
for instruction in preInstruction:
   instructionCount+=1
   print(str(instructionCount) +":" + instruction)
   search =  re.search("move ([0-9]+) from ([0-9]+) to ([0-9]+)",instruction)
   count = int(search.group(1))
   fromIndex = search.group(2)
   toIndex = search.group(3)
   stack[str(toIndex)].extend(stack[str(fromIndex)][-count:])
   for count in range(0,count):
        stack[str(fromIndex)].pop()
   print("-----------")
   for line in stack:
       print(stack[line])
  
for line in stack:
    if(len(stack[line])>0):
        print(stack[line][-1])