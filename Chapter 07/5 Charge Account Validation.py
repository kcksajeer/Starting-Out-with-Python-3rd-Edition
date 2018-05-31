numbers = []

file = open('charge_accounts.txt','r')
for line in file:
    lineList=line.strip()
    itemList=lineList.split(',')
    print(itemList)
file.close()

for i in itemList:
    numbers.append(i)

    
while True:
    user = (input("Please enter a number: "))
    if user in numbers:
        print("Valid!")
    else:
        print("Invalid")    
