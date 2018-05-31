# Rainfall Statistics

rainfall = []

for i in range(5):
    get_rainfall = float(input("Enter monthly rainfall: "))
    rainfall.append(get_rainfall)

print("Total rainfall for the year: ",sum(rainfall))
print("Average rainfall: ",sum(rainfall)/len(rainfall))
print("Maximum: ",max(rainfall))
print("Minimum: ",min(rainfall))
