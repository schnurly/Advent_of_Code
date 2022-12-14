import functools
class vector():
    def __init__(self,x1,y1,x2,y2):        
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2


class vectorizer():
    store=[]
    def reset():
        vectorizer.store=[]
    def reduceFunc(x,y):     
        x1,y1=map(int,x.split(","))
        x2,y2=map(int,y.split(","))
        vectorizer.store.append(vector(x1,y1,x2,y2)) 
        return y
    def generateVectorFromArray(list):
        vectorizer.reset()
        functools.reduce(vectorizer.reduceFunc,list)
        return vectorizer.store

def GetMinMaxVector(vectorList):
    xList=[]
    yList=[]
    for v in vectorList:
        xList.append(v.x1)
        xList.append(v.x2)
        yList.append(v.y1)
        yList.append(v.y2)

    return vector(min(xList),min(yList),max(xList),max(yList))

def readFile(file):  
    retVal=[]
    with open(file,"r") as file:
        for line in file:
             elements=line.strip().split(" -> ")
             retVal.extend(vectorizer.generateVectorFromArray(elements))
    return retVal

def printVector(v):
    print("x:{} y:{} -> x:{} y:{}".format(v.x1,v.y1,v.x2,v.y2))

def createMatrix(xSize,ySize):
    retVal = []
    for y in range(0,ySize):
        row=[]
        for x in range(0,xSize):
            row.append(".")
        retVal.append(row)
    return retVal
def printMatrix(matrix):
    print("---------------")
    for row in matrix:
        print("".join(row))
    print("---------------")
def setRocksToMatrix(matrix,rocks):
    for rock in rocks:
        xL=[rock.x1,rock.x2]
        yL=[rock.y1,rock.y2]
        for x in range(min(xL),max(xL)+1):
            for y in range(min(yL),max(yL)+1):
                matrix[y][x]="#"

def dropSand(matrix,sandX):
    currentX =sandX
    freeY=-1
    for y in range(0,len(matrix)):
        if matrix[y][currentX] != ".":
            freeY=y-1
            break
    if freeY==-1:
        return False
    if(matrix[freeY+1][currentX-1] == "."):  
        diagonalRoll(matrix,freeY+1,currentX-1)
    elif(matrix[freeY+1][currentX+1] == "."):
        diagonalRoll(matrix,freeY+1,currentX+1)
    else:
        matrix[freeY][currentX]="O"
    return True

def diagonalRoll(matrix,yPos,xPos):
     if(matrix[yPos+1][xPos] == "."):
        diagonalRoll(matrix,yPos+1,xPos) 
     elif(matrix[yPos+1][xPos-1] == ".") and xPos-1 >=0 :
        diagonalRoll(matrix,yPos+1,xPos-1)  
     elif(matrix[yPos+1][xPos+1] == ".") and xPos+1 <=len(matrix[0]) :
        diagonalRoll(matrix,yPos+1,xPos+1)  
     else:
        matrix[yPos][xPos]="O"



def simulate(matrix,sandPoint):    
    dropCount=0
    while(True):
        try:
            if(not dropSand(matrix,sandPoint.x1)):
                print("top reached dropCount:"+ str(dropCount))
                return ("top",dropCount)               
            dropCount+=1
        except :
            print("dropCount:"+ str(dropCount))
            return ("border",dropCount)
            

def part_1():
    a=readFile('C:\\temp\\Advent_of_Code\\2022\\14_input.txt')
    sandPoint=vector(500,0,500,0)
    a.append(sandPoint)
    maxMin=GetMinMaxVector(a)
    for v in a:
        v.x1-=maxMin.x1
        v.x2-=maxMin.x1
        v.y1-=maxMin.y1
        v.y2-=maxMin.y1
    a.pop() #remove sandpoint
    printVector(maxMin)
    matrix=createMatrix(maxMin.x2-maxMin.x1+1,maxMin.y2-maxMin.y1+1)
    printMatrix(matrix)
    setRocksToMatrix(matrix,a)
    printMatrix(matrix)
    reason,dropCount=simulate(matrix,sandPoint)
    printMatrix(matrix)
    print("part_1:" + str(dropCount))
def part_2():
    reason="border"
    dropCount=0
    increaseMatrix=50
    while(reason=="border"):
        a=readFile('C:\\temp\\Advent_of_Code\\2022\\14_input.txt')
        sandPoint=vector(500,0,500,0)
        a.append(sandPoint)
        maxMin=GetMinMaxVector(a)
        increaseMatrix+=50
        for v in a:
            v.x1-=maxMin.x1-increaseMatrix
            v.x2-=maxMin.x1-increaseMatrix
            v.y1-=maxMin.y1
            v.y2-=maxMin.y1
        a.pop() #remove sandpoint
        matrix=createMatrix(maxMin.x2-maxMin.x1+1+increaseMatrix*2,maxMin.y2-maxMin.y1+3)
        bottomrock=vector(0,len(matrix)-1,len(matrix[0])-1,len(matrix)-1)
        a.append(bottomrock)
        setRocksToMatrix(matrix,a)
        #printMatrix(matrix)
        reason,dropCount=simulate(matrix,sandPoint)
    #printMatrix(matrix)
    print("part_2:" + str(dropCount))
part_1()
part_2()