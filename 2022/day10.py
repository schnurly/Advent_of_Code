cycle=1
RegisterX=1
signal=0
instructions=[]
def CalcSignal():
    global signal
    signal+=RegisterX*cycle

def IncrementCylce():
    global cycle
    cycle+=1
    if(cycle == 20 or (cycle-20)%40==0):
        CalcSignal()

def AddToRegisterX(value):
    global RegisterX
    RegisterX+=value

def readFile(file):
    global instructions,cycle,RegisterX,signal
    cycle=1
    RegisterX=1
    signal=0
    instructions=[]
    with open(file,"r") as file:
        for line in file:
            instructions.append(line.strip())

def LightPixel(display,cycle):
    global RegisterX
    pos=((cycle-1)%40)
    row=int((cycle-1)/40)
    if(RegisterX-1 <=pos and pos <= RegisterX+1):
        display[row][pos]="#"
    
def part_1():
    for instruction in instructions:      
        if(instruction == "noop"):
            IncrementCylce()
        else:
            a,value=instruction.split(' ')    
            IncrementCylce()
            AddToRegisterX(int(value))
            IncrementCylce()
    print("total cycles: {}".format(cycle))
    print("registerX: {}".format(RegisterX))
    print("strength: {}".format(signal))

def part_2():
    global instructions,cycle,RegisterX,signal
    display=[]
    cycle=1
    RegisterX=1
    signal=0
    instructionCounter=0
    instruction=instructions[instructionCounter]
    for y in range(0,6):
        row=[]
        for x in range(0,40):
            row.append(".")
        display.append(row)
    for instruction in instructions:      
        if(instruction == "noop"):
            LightPixel(display,cycle)
            cycle+=1
        else:
            LightPixel(display,cycle)
            a,value=instruction.split(' ')    
            cycle+=1
            LightPixel(display,cycle)
            AddToRegisterX(int(value))            
            cycle+=1
    for row in display:
        print("".join(row))
    return display

readFile('C:\\temp\\Advent_of_Code\\2022\\10_input.txt.sample')
part_1()
if(signal != 13140):
    print("part1 check failed")
    quit()
display=part_2()
compare=[]
compare.append("##..##..##..##..##..##..##..##..##..##..")
compare.append("###...###...###...###...###...###...###.")
compare.append("####....####....####....####....####....")
compare.append("#####.....#####.....#####.....#####.....")
compare.append("######......######......######......####")
compare.append("#######.......#######.......#######.....")
for i in range(0,len(compare)):
    if(compare[i] != "".join(display[i])):
        print("part2 check failed")
        quit()
readFile('C:\\temp\\Advent_of_Code\\2022\\10_input.txt')
part_1()
part_2()