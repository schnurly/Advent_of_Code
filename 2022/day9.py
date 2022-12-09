instructions=[]
class move:
    def __init__(self,direction,step):
        self.step=step
        self.direction=direction

class position:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class head(position):
     def __init__(self,x,y):
         super().__init__(x,y)
         self.positionCount=1
     def moveX(self,step):
         self.x+=step
         self.positionCount+=1         
     def moveY(self,step):
        self.y+=step
        self.positionCount+=1

class tail(position):
     def __init__(self,x,y):
         super().__init__(x,y)
         self.visitedPos=["0#0"]
     def followHead(self,head):
         diffY=head.y-self.y
         diffX=head.x-self.x
         factorY=1 if diffY >0 else -1
         factorX=1 if diffX >0 else -1
         diffY= diffY*1 if diffY >0 else diffY*-1
         diffX= diffX*1 if diffX >0 else diffX*-1
        #print("tail old pos x:{} y:{}".format(self.x,self.y))
         if(diffY>1 and diffX>0 or diffY>0 and diffX>1):
             self.y+=factorY
             self.x+=factorX        
         elif(diffY>1):
             self.y+=factorY
         elif(diffX>1):
             self.x+=factorX   
         if "{}#{}".format(self.x,self.y) not in self.visitedPos:
            self.visitedPos.append("{}#{}".format(self.x,self.y))
         #print("tail new pos x:{} y:{}".format(self.x,self.y))
class rope():
    def __init__(self):
        self.head=head(0,0)
        self.tail=tail(0,0)

    def move(self,instruction):
        step = 1 if instruction.direction == "U" or instruction.direction == "R" else -1
        for stepIteration in range(0,instruction.step): 
            #print("move {} to {}".format(instruction.step,instruction.direction))
            if instruction.direction == "U" or instruction.direction == "D":
               self.head.moveY(step)               
            else:
               self.head.moveX(step)               
            self.tail.followHead(self.head)
class aNewRope():
    def __init__(self):
        self.head=head(0,0)
        self.tails=[]
        for i in range(0,9):
            self.tails.append(tail(0,0))

    def move(self,instruction):
        step = 1 if instruction.direction == "U" or instruction.direction == "R" else -1
        for stepIteration in range(0,instruction.step): 
            #print("move {} to {}".format(instruction.step,instruction.direction))
            if instruction.direction == "U" or instruction.direction == "D":
               self.head.moveY(step)             
            else:
               self.head.moveX(step)     
            self.tails[0].followHead(self.head)
            for i in range(1,9):              
               self.tails[i].followHead(self.tails[i-1])

def ReadFile(file):
    global instructions
    instructions=[]
    with open(file,"r") as file:
        for line in file:
            direction,step = line.strip().split(" ")
            instructions.append(move(direction,int(step)))   


def DoPart1():
    global instructions 
    ropeObj = rope()
    for instruction in instructions:
        ropeObj.move(instruction)
    return len(ropeObj.tail.visitedPos)

def DoPart2():
    global instructions 
    ropeObj = aNewRope()
    for instruction in instructions:
        ropeObj.move(instruction)
    return len(ropeObj.tails[8].visitedPos)

ReadFile('C:\\temp\\Advent_of_Code\\2022\\09_input.txt.sample')
retVal = DoPart1()
print("part1: tail positions: " + str(retVal))
if(retVal != 13):
    print("validation failed")
    exit()

ReadFile('C:\\temp\\Advent_of_Code\\2022\\09_input.txt.sample2')
retVal = DoPart2()
print("part2: tail positions: " + str(retVal))
if(retVal != 36):
    print("validation failed")
    exit()

ReadFile('C:\\temp\\Advent_of_Code\\2022\\09_input.txt')
retVal = DoPart1()
print("part1: tail positions: " + str(retVal))
retVal = DoPart2()
print("part2: tail positions: " + str(retVal))

