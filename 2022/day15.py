import re
class Sensor():
    offsetX=0
    offsetY=0
    def __init__(self,myPosition,beaconPostition):
        self.myPosition=myPosition
        self.beaconPostition=beaconPostition
        self.MatrixMyPosition=lambda : Position(myPosition.x+Sensor.offsetX,myPosition.y+Sensor.offsetY)
        self.MatrixbeaconPosition=lambda : Position(beaconPostition.x+Sensor.offsetX,beaconPostition.y+Sensor.offsetY)
        self.ManhattenDistance=Sensor.CalcManhattenDistance(self.myPosition,self.beaconPostition)

    def CalcManhattenDistance(position1,position2):
        x=abs(position1.x-position2.x)
        y=abs(position1.y-position2.y)
        return x+y

class Position():
     def __init__(self,x,y): 
         self.x=int(x)
         self.y=int(y)

def readFile(file):  
    retVal=[]
    with open(file,"r") as file:
        for line in file:
             search =  re.search("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): .+ x=(-?[0-9]+), y=(-?[0-9]+)",line.strip())
             posSensor=Position(search.group(1),search.group(2))
             posBeacon=Position(search.group(3),search.group(4))
             sensor=Sensor(posSensor,posBeacon)
             retVal.append(sensor)
    return retVal




def calcOffset(positions):
    minX=(min(positions,key=lambda o:o.myPosition.x)).myPosition.x
    minY=(min(positions,key=lambda o:o.myPosition.y)).myPosition.y
    minX2=(min(positions,key=lambda o:o.beaconPostition.x)).beaconPostition.x
    minY2=(min(positions, key=lambda o:o.beaconPostition.y)).beaconPostition.y
    minX=abs(minX2 if minX2<minX else minX)
    minY=abs(minY2 if minY2<minY else minY)   
    return (minX,minY)

def getMaxPos(positions):
    minX=(max(positions,key=lambda o:o.myPosition.x)).myPosition.x
    minY=(max(positions,key=lambda o:o.myPosition.y)).myPosition.y
    minX2=(max(positions,key=lambda o:o.beaconPostition.x)).beaconPostition.x
    minY2=(max(positions, key=lambda o:o.beaconPostition.y)).beaconPostition.y
    minX=minX2 if minX2>minX else minX
    minY=minY2 if minY2>minY else minY    
    return (minX,minY)

def buildMatrix(xLength,yLength):
    matrix=[]
    for y in range(0,yLength):
        tmp = ["."]*xLength 
        matrix.append(tmp)
    return matrix

def printMatrix(matrix):
   for row in matrix:
       print("".join(row))

def SetSensorBeaconToMatrix(matrix,sensors):
    for sensor in sensors:
        matrix[sensor.MatrixbeaconPosition().y][sensor.MatrixbeaconPosition().x]="B"
        matrix[sensor.MatrixMyPosition().y][sensor.MatrixMyPosition().x]="S"

def CountCoverages(matrix,row):
    return matrix[row].count("#")


def SetCoverageToMatrix(matrix,sensors):
    for y in range(0,len(matrix)):
        for x in range(0,len(matrix[y])):
            if(matrix[y][x]=="."):
                for sensor in sensors:
                    distance=Sensor.CalcManhattenDistance(sensor.MatrixMyPosition(),Position(x,y))                
                    if(distance<=sensor.ManhattenDistance):
                       # print("distance:{} from y:{}x:{} to y:{}x:{}".format(distance,y,x,sensors[0].MatrixMyPosition().y,sensors[0].MatrixMyPosition().x))
                        matrix[y][x]="#"

def SetCoverageToMatrix2(matrix,sensors):   
    for sensor in sensors:
           print("workon: S x:{} y:{}  B x:{} y:{}".format(sensor.MatrixMyPosition().x,sensor.MatrixMyPosition().y,sensor.MatrixbeaconPosition().x,sensor.MatrixbeaconPosition().y))
           distance=sensor.ManhattenDistance
           posY=sensor.MatrixMyPosition().y
           posX=sensor.MatrixMyPosition().x
           lowestY=posY-distance           
           lowestY=0 if lowestY<0 else lowestY
           higestY=posY+distance           
           higestY=len(matrix)-1 if higestY>=len(matrix) else higestY

           lowestX=posX-distance           
           lowestX=0 if lowestX<0 else lowestX
           higestX=posX+distance           
           higestX=len(matrix[0])-1 if higestX>=len(matrix[0]) else higestX

           for y in range(0,distance+1):
               UpPosY=posY-y
               DownPosY=posY+y
               for x in range(0,distance+1-1*y):
                   LeftPosX=posX-x
                   RightPosX=posX+x
                   if(UpPosY>0):
                       if(LeftPosX>=0):
                           if(matrix[UpPosY][LeftPosX]==""):
                               matrix[UpPosY][LeftPosX]="#"
                       if(RightPosX<len(matrix[0])):
                            if(matrix[UpPosY][RightPosX]==""):
                               matrix[UpPosY][RightPosX]="#"
                   if(DownPosY<len(matrix)):
                       if(RightPosX<len(matrix[0])):
                           if(matrix[DownPosY][RightPosX]==""):
                               matrix[DownPosY][RightPosX]="#"
                       if(LeftPosX>=0):
                            if(matrix[DownPosY][LeftPosX]==""):
                               matrix[DownPosY][LeftPosX]="#"

def GetHitsOnRow(sensors,rowNumber,dimensionX,dimensionY):   
    hits=[]   
    ranges=[]
    for sensor in sensors:
           print("workon: S x:{} y:{}  B x:{} y:{}".format(sensor.MatrixMyPosition().x,sensor.MatrixMyPosition().y,sensor.MatrixbeaconPosition().x,sensor.MatrixbeaconPosition().y))
           distance=sensor.ManhattenDistance
           posY=sensor.myPosition.y
           posX=sensor.myPosition.x
           lowestY=posY-distance           
           higestY=posY+distance           
           lowestX=posX-distance                
           higestX=posX+distance                   
           if(lowestY <= rowNumber <=higestY):
               diffY = abs(posY-rowNumber)
               ranges.append(((lowestX+diffY),higestX-diffY))            
               cleanPos=[(sensor.myPosition.x,sensor.myPosition.y),(sensor.beaconPostition.x,sensor.beaconPostition.y)]        
               for posX,posY in cleanPos:         
                 if(posY==rowNumber):
                    if(lowestX+diffY <= posX <= higestX-diffY):
                        if posX not in hits:
                            hits.append(posX)

    print("hits" + str(len(hits)))
    for l,h in sorted(ranges):
        print("{};{}".format(l,h))

    count=0
    for l,h in merge_ranges(ranges):
        count+=abs(l-h)+1

    return count-len(hits)
 
def GetDistressBeacon(sensors,rowNumber,dimensionX,dimensionY):   
    hits=[]   
    ranges=[]
    for sensor in sensors:           
           distance=sensor.ManhattenDistance
           posY=sensor.myPosition.y
           posX=sensor.myPosition.x
           lowestY=posY-distance           
           higestY=posY+distance           
           lowestX=posX-distance                
           higestX=posX+distance                   
           if(lowestY <= rowNumber <=higestY):
               diffY = abs(posY-rowNumber)
               ranges.append(((lowestX+diffY),higestX-diffY))            
               cleanPos=[(sensor.myPosition.x,sensor.myPosition.y),(sensor.beaconPostition.x,sensor.beaconPostition.y)]        
               for posX,posY in cleanPos:         
                 if(posY==rowNumber):
                    if(lowestX+diffY <= posX <= higestX-diffY):
                        if posX not in hits:
                            hits.append(posX)
    retVal=0
    if(len(ranges)>0):
        merged=sorted(merge_ranges(ranges))
        if(len(merged) >=2):
            retVal=merged[0][1]+1        
            for i,j in merged:
                print("{}-{}".format(i,j))         
            
    return retVal

def merge_ranges(ranges):    
    ranges = iter(sorted(ranges))
    current_start, current_stop = next(ranges)
    for start, stop in ranges:
        if start > current_stop:      
            yield current_start, current_stop
            current_start, current_stop = start, stop
        else:         
            current_stop = max(current_stop, stop)
    yield current_start, current_stop

def part_1(file,investigateRow):
    sensors=readFile(file)
    xOffset,yOffset=calcOffset(sensors)
    xMax,yMax=getMaxPos(sensors)
    Sensor.offsetX=xOffset
    Sensor.offsetY=yOffset
    #matrix=buildMatrix(xMax+xOffset+1,yMax+yOffset+1)
    #SetSensorBeaconToMatrix(matrix,sensors)
    #SetCoverageToMatrix2(matrix,sensors)    
    #printMatrix(matrix)
    print("size x:{} y:{}".format(xMax+xOffset+1,yMax+yOffset+1))
    hits=GetHitsOnRow(sensors,investigateRow,xMax+xOffset+1,yMax+yOffset+1)
    print("part_1 line {}: not possible:{}".format(investigateRow,hits))

def part_2(file):
    sensors=readFile(file)
    xOffset,yOffset=calcOffset(sensors)
    xMax,yMax=getMaxPos(sensors)
    Sensor.offsetX=xOffset
    Sensor.offsetY=yOffset

    for investigateRow in range(0,4000001):
        x=GetDistressBeacon(sensors,investigateRow,xMax+xOffset+1,yMax+yOffset+1)
        if(x!=0):
            freq=4000000*x+investigateRow
            print("part_2 tuning frequency:{}".format(freq))
            break
   

#part_1('C:\\temp\\Advent_of_Code\\2022\\15_input.txt.sample',10)
#part_2('C:\\temp\\Advent_of_Code\\2022\\15_input.txt.sample')
#part_1('C:\\temp\\Advent_of_Code\\2022\\15_input.txt',2000000)
part_2('C:\\temp\\Advent_of_Code\\2022\\15_input.txt')