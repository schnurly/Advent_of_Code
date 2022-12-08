matrixSource=[]
matrixVisible=[]

def ReadFile(file):
    global matrixSource,matrixVisible
    matrixSource=[]
    matrixVisible=[]
    with open(file,"r") as file:
        for line in file:
            lineClean = line.strip()
            matrixSource.append(list(map(lambda x: int(x),lineClean)))
            matrixVisible.append(list(map(lambda x: False,lineClean)))

def DetermineVisibleTrees():
    global matrixSource,matrixVisible
    #top
    for x in range(0,len(matrixSource[0])):  
        highestPos=matrixSource[0][x]
        for y in range(1,len(matrixSource)):
            if(matrixSource[y][x] > highestPos):
                matrixVisible[y][x]=True
                highestPos=matrixSource[y][x]  
    #left
    for y in range(0,len(matrixSource)):
        highestPos=matrixSource[y][0]
        for x in range(1,len(matrixSource[0])):
            if(matrixSource[y][x] > highestPos):
                matrixVisible[y][x]=True
                highestPos=matrixSource[y][x]             
    #right
    for y in range(0,len(matrixSource)):
        highestPos=matrixSource[y][len(matrixSource[0])-1]
        for x in range(len(matrixSource[0])-2,-1,-1):
            if(matrixSource[y][x] > highestPos):
                matrixVisible[y][x]=True
                highestPos=matrixSource[y][x]           
    #buttom
    for x in range(0,len(matrixSource[0])):
        highestPos=matrixSource[len(matrixSource)-1][x]
        for y in range(len(matrixSource)-2,-1,-1):    
            if(matrixSource[y][x] > highestPos):
                matrixVisible[y][x]=True
                highestPos=matrixSource[y][x]  
            
    #set borders
    for x in range(0,len(matrixSource[0])):
        matrixVisible[0][x]=True
        matrixVisible[len(matrixSource)-1][x]=True
    for y in range(0,len(matrixSource)):
        matrixVisible[y][0]=True
        matrixVisible[y][len(matrixSource[y])-1]=True        

def CountVisible():
    global matrixVisible
    trueCount=0
    for row in  matrixVisible:
        for col in row:
            trueCount= trueCount+1 if col else trueCount        
    return trueCount

def DoScoreCalcForTree(xPos,yPos,high):
    global matrixSource 
    toptreeCount=0
    lefttreeCount=0
    righttreeCount=0
    downtreeCount=0
    # to top  
    for y in range(yPos-1,-1,-1):         
        toptreeCount+=1
        if(matrixSource[y][xPos] >= high):
            break   
    #to left
    for x in range(xPos-1,-1,-1):
        lefttreeCount+=1
        if(matrixSource[yPos][x] >= high):          
            break
  
    #to right
    for x in range(xPos+1,len(matrixSource[yPos])):        
        righttreeCount+=1
        if(matrixSource[yPos][x] >= high):          
            break

    #to buttom
    for y in range(yPos+1,len(matrixSource)):
        downtreeCount+=1
        if(matrixSource[y][xPos] >= high):            
            break
  
    #print(str(xPos) + " " + str(yPos) + " ### " + str(toptreeCount) + "*" + str(lefttreeCount) + "*" + str(righttreeCount) + "*" + str(downtreeCount))
    return toptreeCount * lefttreeCount * righttreeCount * downtreeCount

def CalcHighestScore():
    global matrixSource
    highest=0
    for y in range(0,len(matrixSource)):
        for x in range(0,len(matrixSource[y])):
            result = DoScoreCalcForTree(x,y,matrixSource[y][x])            
            highest = result if result > highest else highest
    return highest

def DoPart1():
    DetermineVisibleTrees()
    return CountVisible()
def DoPart2():
    return CalcHighestScore()
    

ReadFile('C:\\temp\\Advent_of_Code\\2022\\08_input.txt.sample')
result = DoPart1()
if(result != 21):
    print("ValidationFailed:" + str(result) )
    for row in  matrixVisible:
        print(list(map(lambda x: "O" if x else "X",row)))
<<<<<<< HEAD
result = DoPart2()
=======
result = CalcHighestScore()
>>>>>>> 6636abf0d4fce63994d9e79a05316afdf7cc0041
if(result != 8):
    print("ValidationFailed Part2:" + str(result) )
    exit()

ReadFile('C:\\temp\\Advent_of_Code\\2022\\08_input.txt')
result = DoPart1()
print("visible:" + str(result))
<<<<<<< HEAD
result = DoPart2()
print("score:" + str(result))
=======
result = CalcHighestScore()
print("score:" + str(result))
>>>>>>> 6636abf0d4fce63994d9e79a05316afdf7cc0041
