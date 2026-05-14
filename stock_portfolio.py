stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]
        investment = price * quantity

        total_investment += investment

        print(stock_name, "x", quantity, "=", investment)

    else:
        print("❌ Stock not found")

print("\n💰 Total Investment Value =", total_investment)

# Save result to file
file = open("portfolio.txt", "w")

file.write("Total Investment Value = " + str(total_investment))

file.close()

print("📁 Result saved in portfolio.txt")