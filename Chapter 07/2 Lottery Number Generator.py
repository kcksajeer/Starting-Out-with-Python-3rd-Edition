#Lottery Number Generator

import random

numList = []

for i in range(7):
    randNum = random.randint(0000000,9999999)
    numList.append(randNum)

for i in numList:
    print (i)

