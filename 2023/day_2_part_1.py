import re

def doPart1(filePath):
    sum = 0
    with open(filePath,"r") as file:
        for line in file:
           id = GetGameId(line.strip())
           isgood = IsGoodGame(line.strip())
           if(isgood):
               sum+=int(id)
    print(f"the searched value is {sum}")

def doPart2(filePath):
    sum = 0
    with open(filePath,"r") as file:
        for line in file:           
           sum += IsGoodGame2(line.strip())          
    print(f"the searched value is {sum}")

def GetGameId(line):
    search  = re.search(r"Game ([0-9]+):",line)
    return search.group(1)

def IsGoodGame(line):
    countdic = {"red":0,"green":0,"blue":0}
    linereduced = re.sub("Game [0-9]+:","",line)
    packs = linereduced.split(";")
    for pack in packs:
        parcels = pack.split(",")
        for parcel in parcels:        
            count,color=parcel.strip().split(" ")
            count = int(count)
            countdic[color]=count
            if(countdic["red"] > 12 or countdic["green"]  > 13 or countdic["blue"]  > 14):    
                return False
   
    return True

def IsGoodGame2(line):
    countdic = {"red":0,"green":0,"blue":0}
    linereduced = re.sub("Game [0-9]+:","",line)
    packs = linereduced.split(";")
    for pack in packs:
        parcels = pack.split(",")
        for parcel in parcels:        
            count,color=parcel.strip().split(" ")
            count = int(count)
            if(countdic[color]<count):
                countdic[color]=count

   
    return   countdic["red"]*countdic["green"]*countdic["blue"]  

#doPart1('C:\\temp\\Advent_of_Code\\2023\\02_input.txt.sample')
doPart2('C:\\temp\\Advent_of_Code\\2023\\02_input.txt')