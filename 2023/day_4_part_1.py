import re

def doPart1(filePath):
    sum=0
    with open(filePath,"r") as file:
        for line in file:
           count =countMatches(line.strip())  
           if(count >0):
               print(f"{pow(2,count-1)}")           
               sum+=pow(2,count-1)
    print(f"part 1 sum:{sum}")

def doPart2(filePath):
    cards = []
    count = 0
    with open(filePath,"r") as file:
        for line in file:
           cards.append(countMatches(line.strip()))  
    for i in range(len(cards)):
        count+=playRecursiv(cards,i)
    print(f"part 2 count:{count}")

def playRecursiv(cardsBase,index):
    countMatches = cardsBase[index]
    playedCards = 1
    if(countMatches >0):
        for i in range(index+1,index+countMatches+1):
             playedCards+=playRecursiv(cardsBase,i)        
    return playedCards
   

def countMatches(line):
    linereduced = re.sub("Card +[0-9]+:","",line).strip()
    winningNumber,playedNumber = linereduced.split("|")
    matches=0
    for pNumber in playedNumber.strip().split(" "):
        for wNumber in winningNumber.strip().split(" "):
            if(pNumber == wNumber and wNumber != ""):
                matches+=1
                break
    return matches
#doPart1('C:\\temp\\Advent_of_Code\\2023\\04_input.txt')
from time import *
t1 = process_time() 
doPart2('C:\\temp\\Advent_of_Code\\2023\\04_input.txt')
t2 = process_time()
t = t2 - t1

print('Rechenzeit: ', t)
