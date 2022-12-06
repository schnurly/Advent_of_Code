with open('C:\\temp\\Advent_of_Code\\2022\\06_input.txt',"r") as file:
    input=file.read()

validationPattern = []

index=0
for char in input:
    validationPattern.append(char)
    if(len(validationPattern)>14):
        validationPattern.pop(0)
    if(len(validationPattern)==14):
        if(index > 6):
            charCounter = {}
            for c in validationPattern:
                if c not in charCounter:
                    charCounter[c] =0
                charCounter[c]+=1
            isValid=True
            for c in charCounter:
                if(charCounter[c]>1):
                    isValid=False
            if(isValid):
                print("found on index " +str(index))
                print(index+1)
                print(validationPattern)
                break
    index+=1