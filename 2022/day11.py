import re
import functools

class monkey():
    def __init__(self,id):        
        self.divisible=None 
        self.goodMonkey=None
        self.badMonkey=None
        self.items = []
        self.id=id
        self.inspectedCount=0

    def print(self):
        print("Monkey:{}".format(self.id))
        print(self.items)
        print("inspected:{}".format(self.inspectedCount))
    def SetOperation(self,operation):
          search =  re.search("old ([+|*]) (.+)",operation)
          op = search.group(1)
          val = search.group(2)
          if(op == "+"):
              if(val=="old"):
                  self.operation=lambda x : x+x
              else:
                  self.operation= lambda x : x + int(val)
          else:
              if(val=="old"):
                  self.operation= lambda x : x*x
              else:
                  self.operation= lambda x : x*int(val)
        
    def Inspect(self,HandOverHandler):
        while(len(self.items) > 0):
            self.inspectedCount+=1
            item = self.items.pop()
            itemVal = int((int(self.operation(item)))/3)
            if(itemVal%self.divisible==0):
                HandOverHandler(self.goodMonkey,itemVal)
            else:
                HandOverHandler(self.badMonkey,itemVal)
    def InspectDontWorryBeHappy(self,HandOverHandler,commonDivisor):
        while(len(self.items) > 0):
            self.inspectedCount+=1
            item = self.items.pop()
            itemVal = int(self.operation(item))
            itemVal = itemVal%commonDivisor
            if(itemVal%self.divisible==0):
                HandOverHandler(self.goodMonkey,itemVal)
            else:
                tmp=itemVal%self.divisible
                HandOverHandler(self.badMonkey,itemVal)  

monkeys=[]
def HandOverHandler(monkeyIndex,item):
    global monkeys
    #print("to monkey {} -> {}".format(monkeyIndex,item))
    monkeys[monkeyIndex].items.append(item)

import re
def ReadFile(file):
    global instructions
    monkeys=[]
    monkeyIndex=0
    with open(file,"r") as file:
        monkeyInstance=None
        for line in file:
            cleaned = line.strip()
            if re.match("Monkey ([0-9]+):",cleaned): 
                search =  re.search("Monkey ([0-9]+):",cleaned)
                monkeyInstance=monkey(monkeyIndex)
                monkeys.append(monkeyInstance)
                monkeyIndex+=1
            elif re.match("Starting items:(.+)",cleaned): 
                search =  re.search("Starting items:(.+)",cleaned)
                monkeyInstance.items=list(map(int,map(str.strip,search.group(1).split(","))))
            elif re.match("Operation: new = ",cleaned):   
                search =  re.search("Operation: new = (.+)",cleaned)
                monkeyInstance.SetOperation(search.group(1))
            elif re.match("Test: divisible by ([0-9]+)",cleaned):   
                search =  re.search("Test: divisible by ([0-9]+)",cleaned)
                monkeyInstance.divisible=int(search.group(1).strip())               
            elif re.match("If true:.+([0-9]+)",cleaned):  
                search =  re.search("If true:.+([0-9]+)",cleaned)
                monkeyInstance.goodMonkey=int(search.group(1))
            elif re.match("If false:.+([0-9]+)",cleaned):  
                search =  re.search("If false:.+([0-9]+)",cleaned)
                monkeyInstance.badMonkey=int(search.group(1))
    return monkeys


    
def MultiplyHighestInspectionCounts(monkeys):
    inspectedCounts=[]
    for monkeyInstance in monkeys:
        inspectedCounts.append(monkeyInstance.inspectedCount)
    first=max(inspectedCounts)
    inspectedCounts.remove(first)
    second=max(inspectedCounts)
    return first*second

monkeys=ReadFile('C:\\temp\\Advent_of_Code\\2022\\11_input.txt.sample')
for i in range(0,20):
    for monkeyInstance in monkeys:
        monkeyInstance.Inspect(HandOverHandler)        

if(MultiplyHighestInspectionCounts(monkeys)!=10605):
    print("part1 check failed")
    quit()
monkeys=ReadFile('C:\\temp\\Advent_of_Code\\2022\\11_input.txt.sample')
common_divisor = functools.reduce(lambda y, x: y* x, (m.divisible for m in monkeys))
for i in range(0,10000):
    for monkeyInstance in monkeys:
        monkeyInstance.InspectDontWorryBeHappy(HandOverHandler,common_divisor)      
part2Sum=MultiplyHighestInspectionCounts(monkeys)
print("part2sum:{}".format(part2Sum))

print("-------------------")
monkeys=ReadFile('C:\\temp\\Advent_of_Code\\2022\\11_input.txt')
for i in range(0,20):
    for monkeyInstance in monkeys:
        monkeyInstance.Inspect(HandOverHandler)  
 
part1Sum=MultiplyHighestInspectionCounts(monkeys)
print("part1sum:{}".format(part1Sum))
monkeys=ReadFile('C:\\temp\\Advent_of_Code\\2022\\11_input.txt')
common_divisor = functools.reduce(lambda cd, x: cd * x, (m.divisible for m in monkeys))
for i in range(0,10000):
    for monkeyInstance in monkeys:
        monkeyInstance.InspectDontWorryBeHappy(HandOverHandler,common_divisor)    
part2Sum=MultiplyHighestInspectionCounts(monkeys)
print("part2sum:{}".format(part2Sum))
