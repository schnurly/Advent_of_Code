from queue import PriorityQueue

lines = [line.strip() for line in open('input15.txt', 'r').readlines()]
matrix = [[int(char) for char in line]  for line in lines] 
width=len(matrix[0])
height = len(matrix)

#X,Y
motions = [(0,1),(0,-1),(-1,0),(1,0)]



def findLowRisk(map):   
    startPos = (0,0)
    lastPos = (len(map[0])-1,len(map)-1)
    riskMap = {}
    riskMap[startPos] = 0
    camefrom = {startPos: None}
    queue = PriorityQueue()
    queue.put((0,startPos))
    pos = None
    while not queue.empty():
        currentPos = queue.get()[1]    
        if currentPos == lastPos:
            break
        for motion in motions:           
            newPos = (currentPos[0]+motion[0],currentPos[1]+motion[1])
            if 0 <= newPos[0] < len(map[0]) and 0 <= newPos[1] <  len(map):
                newrisk =  riskMap[currentPos] + map[newPos[1]][newPos[0]]
                if newPos not in camefrom or newrisk < riskMap[newPos]:
                    riskMap[newPos] = newrisk
                    camefrom[newPos] = currentPos
                    queue.put((newrisk,newPos))
    return riskMap[currentPos]

def part2(map):
    width=len(map[0])
    height = len(map)
    for i in range(4):
        for line in map:
            rightpart = [ x % 9 + 1 for x in line[-width:]]
            line.extend(rightpart)
        for line in map[height*i:height*(i+1)]:
            newline = [ x % 9 + 1 for x in line]
            map.append(newline)

    return findLowRisk(map)
print(findLowRisk(matrix))
print(part2(matrix))


