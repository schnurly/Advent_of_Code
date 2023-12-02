from math import fabs
import re
def doPart1(filePath):
    sum = 0
    with open(filePath,"r") as file:
        for line in file:
           sum +=extracNumbers(line.strip())
    print(f"the searched value is {sum}")
 
def extracNumbers(text):
    firstNumber = ""
    secondNumber = ""
    for chr in text:
        if(re.search(r'[0-9]',chr)):
            if(firstNumber == ""):
                firstNumber = chr
            else:
                secondNumber = chr
    if(secondNumber == ""):
        secondNumber = firstNumber
    return int(firstNumber + secondNumber)

def doPart2(filePath):
    sum = 0
    with open(filePath,"r") as file:
        for line in file:
           sum +=extracNumbersAdvanced(line.strip())
    print(f"the searched value is {sum}")
 
numberdecoding = ["null","one","two","three","four","five","six","seven","eight","nine"]

def extracNumbersAdvanced(text):
    firstNumber = ""
    firstIndex = len(text)
    secondNumber = ""
    secondIndex = -1
    indexList = {}
    for i in range(len(numberdecoding)):
        try:
            index=-1
            while(True):
                index = text.index(numberdecoding[i],index+1)
                indexList[index] = i 
        except:
            pass
    if(len(indexList)>0):
        firstIndex = min(indexList)
        firstNumber = indexList[min(indexList)]
        secondIndex = max(indexList)
        secondNumber = indexList[max(indexList)]
    
    for i in range(len(text)):
        chr = text[i]
        if(re.search(r'[0-9]',chr)):
            if( firstIndex > i ):
                firstNumber = chr
                firstIndex = i
            elif(secondIndex < i):
                secondNumber = chr
                secondIndex = i
    if(secondNumber == ""):
        secondNumber = firstNumber
    #print(f"{firstNumber}{secondNumber}")
    print(f"{text}#{firstNumber}{secondNumber}")
    return int(f"{firstNumber}{secondNumber}")


#doPart1('C:\\temp\\Advent_of_Code\\2023\\01_input.txt.sample')
##doPart1('C:\\temp\\Advent_of_Code\\2023\\01_input.txt')
#doPart2('C:\\temp\\Advent_of_Code\\2023\\01_input.txt.sample2')
doPart2('C:\\temp\\Advent_of_Code\\2023\\01_input.txt')

