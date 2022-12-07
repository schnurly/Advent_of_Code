class cdir:
    def __init__(self,name):
        self.name = name
        self.parent  =None
        self.files = []
        self.subDirs = []

class cfile:
    def __init__(self,name,size):
        self.name = name
        self.size = size

rootDir = cdir("/")
currentDir = None
with open('C:\\temp\\Advent_of_Code\\2022\\07_input.txt',"r") as file:
    lines = []
    
    for line in file:
        cmd = line.strip()
        if(cmd == "$ cd /"):
            currentDir = rootDir
        elif(cmd.startswith("dir")):
            name = cmd.split(" ")[1]
            dirExists=False
            for d in currentDir.subDirs:
                if(d.name == name):
                    dirExists=True
                    print("d exists")
            if(dirExists == False):
                tmpDir = cdir(name)
                tmpDir.parent = currentDir
                currentDir.subDirs.append(tmpDir)
        elif(cmd.startswith("$ cd")):
            if(cmd.startswith("$ cd ..")):
                currentDir = currentDir.parent
            else:
                name = cmd.split(" ")[2]
                for d in currentDir.subDirs:
                    if(d.name == name):
                        currentDir = d   
        elif(cmd.startswith("$ ls")):
            pass
        else:      
            fileSize,fileName = cmd.split(" ")
            if(fileSize == ""):
                break
            fileExists=False
            for f in currentDir.files:
                if(fileName==f.name):
                    fileExists=True
                    print("f exists")
            if(fileExists==False):
                currentDir.files.append(cfile(fileName,int(fileSize)))



logging=[]
def parse(dir,level):
    dirSum=0   
    for d in dir.subDirs:
        dirSum+=parse(d,level+1)
    fileSum=0
    print("#"*level+ dir.name)
    for f in dir.files:
        print("  "+f.name)
        fileSum+=f.size
    dirSum+=fileSum
    print("#"*level+ dir.name + " | " + str(fileSum) + " | " + str(dirSum))
    return dirSum

fullsize= parse(rootDir,1)
needToFree = 30000000 -(70000000 - fullsize)
print("need size:"+ str(needToFree))

def parse2(dir,level):
    global logging
    global needToFree
    dirSum=0   
    for d in dir.subDirs:
        dirSum+=parse2(d,level+1)
    fileSum=0
    for f in dir.files:    
        fileSum+=f.size
    dirSum+=fileSum
    if(needToFree < dirSum and dirSum < needToFree+10000):
        logging.append("matched:" + str(dirSum) + " " + dir.name)
    return dirSum

parse2(rootDir,1)

for l in logging:
    print(l)