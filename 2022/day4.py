def compare(part1,part2):
    retVal = False
    p1Left,p1Right = map(int,part1.split("-"))
    p2Left,p2Right = map(int,part2.split("-"))
    if p1Left <= p2Left and p2Right <= p1Right:
        print("contains " + part1 + " " + part2)
        retVal = True
    if p1Left >= p2Left and p2Right >= p1Right:    
        print("contains " + part1 + " " + part2)
        retVal = True
    return retVal

count=0
with open('C:\\temp\\aoc_2022\\04_input.txt',"r") as file:
    lines = []
    for line in file:
        arr = line.strip().split(",")
        if compare(arr[0],arr[1]):
            count+=1
print(count)