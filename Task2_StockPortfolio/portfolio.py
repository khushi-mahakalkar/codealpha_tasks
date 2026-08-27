print("=" * 50)
print("              SMART PORTFOLIO TRACKER")
print("=" * 50)
print("     Track your investments easily with Python!")
print("=" * 50)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

print("\nEnter the stocks you want to add to your portfolio.")
print("Type 'done' when you have finished.")

while True:

    stock = input("\nEnter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    if stock in portfolio:
        print("This stock is already in your portfolio.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity

    portfolio[stock] = {
        "quantity": quantity,
        "price": stock_prices[stock],
        "investment": investment
    }

    total_investment += investment

    print(f"{stock} added successfully!")
    print(f"Investment in {stock}: ${investment}")

print("\n" + "=" * 50)
print("                PORTFOLIO SUMMARY")
print("=" * 50)

if not portfolio:
    print("No stocks were added to the portfolio.")

else:
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 50)

    for stock, details in portfolio.items():
        print(
            f"{stock:<10}"
            f"{details['quantity']:<12}"
            f"${details['price']:<11}"
            f"${details['investment']:<15}"
        )

    print("-" * 50)
    print(f"Total Investment: ${total_investment}")

if portfolio:

    save_file = input("\nDo you want to save this portfolio? (yes/no): ").lower()

    if save_file == "yes":

        try:
            with open("portfolio_report.txt", "w") as file:

                file.write("SMART PORTFOLIO TRACKER\n")
                file.write("=" * 40 + "\n\n")

                for stock, details in portfolio.items():
                    file.write(
                        f"{stock} | Quantity: {details['quantity']} | "
                        f"Price: ${details['price']} | "
                        f"Investment: ${details['investment']}\n"
                    )

                file.write("\n" + "=" * 40 + "\n")
                file.write(f"Total Investment: ${total_investment}\n")

            print("Portfolio saved successfully as 'portfolio_report.txt'.")

        except PermissionError:
            print("Unable to save the file in this online compiler.")
            print("Your portfolio calculation is still complete.")

print("\nThank you for using Smart Portfolio Tracker!")
print("=" * 50)
