stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock = input("\nEnter stock name (or type 'DONE' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    while True:
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n" + "=" * 40)
print("        PORTFOLIO SUMMARY")
print("=" * 40)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock}")
    print(f"Quantity : {quantity}")
    print(f"Price    : ${price}")
    print(f"Value    : ${value}")
    print("-" * 30)

print(f"\nTotal Investment Value = ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 35 + "\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(f"{stock}\n")
        file.write(f"Quantity : {quantity}\n")
        file.write(f"Price    : ${price}\n")
        file.write(f"Value    : ${value}\n")
        file.write("-" * 25 + "\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio summary has been saved to 'portfolio_summary.txt'.")
print("\nThank you for using the Stock Portfolio Tracker!")