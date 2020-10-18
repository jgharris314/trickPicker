from random import randint
import csv

#Generating the trick dictionary from a text file and various extra dictionaries to be used later
trickList = []
with open('tricks.csv', newline='') as tricks:
    reader = csv.reader(tricks, delimiter=',')
    for i in tricks:
        trickList.append(i)

trickList = [i.strip('\r\n') for i in trickList]

trickDict = {}

for i in range(len(trickList)):
    trickDict[i] = trickList[i]


tempDict = trickDict.copy()
usedList = []
currentTrick = ''
remainingList = trickList.copy()

# rollEm chooses a random trick from the dictionary of tricks and displays the chosen one, removing it from the pool
# so a trick can only be chosen once until all tricks have been chosen.

def rollEm():
    global tempDict
    global trickDict
    global usedList
    global currentTrick
    global remainingList
    trickNum = randint(0, len(trickDict) - 1)
    running = True
    while running:
        if trickNum not in tempDict:
            if len(tempDict) == 0:
                tempDict = trickDict.copy()
                usedList = []
                remainingList = trickList.copy()
                pass
            else:
                trickNum = randint(0, len(trickDict) - 1)
                pass
        else:
            currentTrick = trickDict[trickNum]
            usedList.append(currentTrick)
            remainingList.remove(trickDict[trickNum])
            tempDict.pop(trickNum)
            break



