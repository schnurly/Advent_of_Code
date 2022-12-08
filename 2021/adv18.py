

def initDataset(input):
    retVal = []
    for line in input:
        retVal.append(eval(line))
    return retVal

def countPairs(input):
    subpairs = 0
    onlyArray = True
    pairs = 1
    for i in range(0, 2):
        if( isinstance(input[i], list)):
            subpairs += countPairs(input[i] )   
        else:
            onlyArray = False
    if(onlyArray):
       pairs = 0
    return pairs  +subpairs


def explode(input):
    if( not isinstance(input[0], list) and not isinstance(input[0], list) ):
        return None
    else:
        if(isinstance(input[0], list)):
            recurseResult = explode(input[0])
            if(recurseResult is None):
                recurseResult = [input,input.pop(0)] 
                input.insert(0,0)
   

        

print(countPairs(eval('[1,2]')))
print(countPairs(eval('[[1,2],3]')))
print(countPairs(eval('[[[[1,2],[3,4]],[[5,6],[7,8]]],9]')))
print(explode(eval('[[[[[9,8],1],2],3],4]')))




input = open('c:\\temp\\advent_input18_2.txt', 'r').readlines()
test = initDataset(input)