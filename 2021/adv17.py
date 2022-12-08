class Target:
    def __init__(self,XLow,XHigh,YLow,YHigh):
        self.XLow = XLow
        self.XHigh = XHigh
        self.YLow = YLow
        self.YHigh = YHigh

    def IsHit(self,x,y):
        retVal = False
        if(self.XLow <= x <= self.XHigh and self.YLow <= y <= self.YHigh):
            retVal = True
        return retVal
    def IsMissed(self,x,y):
        retVal = False
        if(y < self.YLow or x > self.XHigh ):
            retVal = True
       
        return retVal

target = Target(128,160,-142,-88)
#target = Target(20,30,-10,-5)
start = (0,0)
velocity = (6,3)
position = start

found = False
def shoot(position,velocity):
    highestY = 0
    while found == False:
        highestY = position[1] if position[1] > highestY else highestY
        position = (position[0]+velocity[0],position[1]+velocity[1])
        #print("Try at x:",position[0], "y:",position[1])
        if(target.IsHit(position[0],position[1])):
            #print("Hit at x:",position[0], "y:",position[1])
            break
        if(target.IsMissed(position[0],position[1])):
            #print("Missed")
            highestY = -1
            break
        xFactor = 1 if velocity[0] >0 else 0
        velocity  = (velocity[0]-xFactor,velocity[1]-1)
    return highestY

bestY =0
bestVelocity =()

i=0
xFrom =0
xTo = 0
xrange = 0
while xrange <= target.XHigh:    
    i+=1
    xrange =  sum(range(1,i+1))
    if xrange >= target.XLow and xFrom == 0 :
        xFrom = i
    if xrange > target.XHigh:
        xTo = i-1

def part1():
    for x in range(xFrom,xTo):
        for y in range(1,500):
            print("y:",y)
            yresult = shoot(start,(x,y))
            if yresult > bestY:
                bestY = yresult
                bestVelocity=(x,y)

    print("Max High:",bestY , " by velocity x:",bestVelocity[0]," y:",bestVelocity[1])

hit=0

for x in range(xFrom,target.XHigh+1):
    for y in range(1,1000,1):
        yresult = shoot(start,(x,y-500))
        if yresult > -1:
            print(x,",",y-500)
            hit+=1
print("hits:",hit)
