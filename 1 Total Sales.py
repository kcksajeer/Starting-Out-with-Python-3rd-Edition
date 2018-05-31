daily_sales = []

for i in range(7):
    sales = float(input("Please enter the todays sales: "))
    daily_sales.append(sales)

print ("Sum is",sum(daily_sales))
