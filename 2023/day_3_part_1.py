import re

def doPart1(filePath):
    matrix = []
    with open(filePath,"r") as file:
        for line in file:
           matrix.append(line.strip())
    doWork(matrix)
  

def doWork(matrix):
    symbolPositions = []
    numberPositions= []
    for rowIndex in range(len(matrix)):
        number = ""
        indexStart = 0
        lastcolIndex = 0
        for colIndex in range(len(matrix[rowIndex])):
            if(not re.match("[0-9]|\.",matrix[rowIndex][colIndex])):        
                #print(f"symbol {matrix[rowIndex][colIndex]} y:{rowIndex} x:{colIndex}")
                symbolPositions.append((rowIndex,colIndex,matrix[rowIndex][colIndex]))
            if(re.match("[0-9]",matrix[rowIndex][colIndex])):
                if(number == ""):
                    indexStart = colIndex
                number+=matrix[rowIndex][colIndex]; 
            elif(number != ""):
                numberPositions.append((number,rowIndex,indexStart,lastcolIndex))
                number = ""
            lastcolIndex = colIndex
        if(number != ""):
            numberPositions.append((number,rowIndex,indexStart,lastcolIndex))
    sum=0
    for numberpos in numberPositions:
        for symbolpos in symbolPositions:
            number = int(numberpos[0])
            y = numberpos[1]
            xStart = numberpos[2]
            xEnd = numberpos[3]        
            if(  y-1 <= symbolpos[0] <= y+1  ):
                #print(f"Y{number}:{y}:{xStart}:{xEnd}")  
                if((xStart-1<= symbolpos[1]  <= xEnd+1)):           
                    #print(f"({y},{xStart},{xEnd},{number})")    
                    sum+=number
                    break
    print(f"part 1 sum:{sum}")               
    sum =0
   
    for symbolpos in symbolPositions:        
        if(symbolpos[2] == "*"):
            count = 0
            subsum=0
            for numberpos in numberPositions:
                number = int(numberpos[0])
                y = numberpos[1]
                xStart = numberpos[2]
                xEnd = numberpos[3]        
                if(  y-1 <= symbolpos[0] <= y+1  ):
                    #print(f"Y{number}:{y}:{xStart}:{xEnd}")  
                    if((xStart-1<= symbolpos[1]  <= xEnd+1)):           
                        #print(f"({y},{xStart},{xEnd},{number})")    
                        count+=1
                        if(subsum ==0):
                            subsum=number
                        else:
                            subsum=subsum*number
            if(count == 2):
                sum+=subsum
    print(f"part 2 sum:{sum}")               
#doPart1('C:\\temp\\Advent_of_Code\\2023\\03_input.txt.sample')
doPart1('C:\\temp\\Advent_of_Code\\2023\\03_input.txt')
