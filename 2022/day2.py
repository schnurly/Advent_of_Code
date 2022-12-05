def getItem(item):
    switcher = {
          "A" : "Rock",
          "B" : "Paper",
          "C" : "Scissors",
          "Y" : "Paper",
          "X" : "Rock",
          "Z" : "Scissors"
        }
    return switcher.get(item)

def getItemValue(item):
     switcher = {
          "Rock" : 1,
          "Paper" : 2,
          "Scissors" : 3
        }
     return switcher.get(item)

def getWinner(player1,player2):
    if(player1 == player2):
        return 0
    if((player1 == "Rock") and (player2 == "Paper")):
        return 1
    if((player1 == "Rock") and (player2 == "Scissors")):
        return -1
    if((player1 == "Paper") and (player2 == "Rock")):
        return -1
    if((player1 == "Paper") and (player2 == "Scissors")):
        return 1
    if((player1 == "Scissors") and (player2 == "Rock")):
        return 1
    if((player1 == "Scissors") and (player2 == "Paper")):
        return -1

myPoints=0
with open('C:\\temp\\aoc_2022\\02_input.txt',"r") as file:
    for line in file:
        enemy,me = map(getItem,line.rstrip().split(' '))
        winner = getWinner(enemy,me)
        if(winner == 1):
           myPoints+=6
        elif (winner == 0):
            myPoints+=3
        myPoints+=getItemValue(me)

print(myPoints)