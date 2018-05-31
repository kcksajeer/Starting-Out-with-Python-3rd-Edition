numbers = []

for i in range(5):
    inputNum = float(input("Please enter a number: "))
    numbers.append(inputNum)

print("Lowest: ",min(numbers))
print("Highest: ",max(numbers))
print("Total: ",sum(numbers))
print("Average: ",sum(numbers)/len(numbers))
