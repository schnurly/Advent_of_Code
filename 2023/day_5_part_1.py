import re

seeds=[]
seedsPart2 = []
blocks={}
blockString=""

def doPart1(filePath):
    sum=0
    with open(filePath,"r") as file:
        for line in file:
            DoInit(line.strip())
    CalcLowestLocation()    

def doPart2(filePath):
    sum=0
    with open(filePath,"r") as file:
        for line in file:
            DoInit(line.strip())
    CalcLowestLocationPart2()  

def CalcLowestLocationPart2():
    lowestSeed=0
    for seedStart,seedRange in seedsPart2:
        #print(f"seedstart:{seedStart} seedrange:{seedRange}")
        for seed in range(seedStart,seedStart+seedRange):
            newseed = DoMapChain(seed)
            if(lowestSeed==0):
                lowestSeed = newseed
            elif(lowestSeed>newseed):
                lowestSeed = newseed
            #print(f"old:{seed} new:{newseed}")
    print(f"part 2 min location value {lowestSeed}")

def CalcLowestLocation():
    newlocation = []
    for seed in seeds:
        newseed = DoMapChain(seed)
        newlocation.append(newseed)
        #print(f"old:{seed} new:{newseed}")
    print(f"min location value {min(newlocation)}")

def DoMapChain(seed):
     global blocks
     newseed = seed
     for key in blocks:  
        newseed = Remap(newseed,key)
     return newseed

def DoInit(line):     
    global seeds, blocks, blockString, seedsPart2   
    if(line.startswith("seeds:")):
        seeds= [int(x) for x in line.replace("seeds: ","").split(" ")]
        n = 2
        seedsPart2 = [seeds[i:i+n] for i in range(0,len(seeds),n)]
    elif(line.endswith("map:")):
        blockString = line
        blocks[blockString] = []
    elif(line != ""):
        dest,source,dataRange=line.split(" ")
        blocks[blockString].append((int(source),int(dest),int(dataRange)))

def Remap(seed,blockName):
    global blocks
    block = blocks[blockName]
    newSeed = seed
    for source,dest,dataRange in block:
        if(source <= seed <source+dataRange):
            seedOffset = seed -source
            newSeed = dest+seedOffset
            break
    return newSeed


#doPart1('C:\\temp\\Advent_of_Code\\2023\\05_input.txt.sample')
#doPart1('C:\\temp\\Advent_of_Code\\2023\\05_input.txt')
#doPart2('C:\\temp\\Advent_of_Code\\2023\\05_input.txt.sample')
doPart2('C:\\temp\\Advent_of_Code\\2023\\05_input.txt')