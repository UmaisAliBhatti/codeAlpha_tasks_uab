# prices are fixed, I just typed them in by hand

prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
}

print("Stock Portfolio Tracker")
print("Available stocks:", list(prices.keys()))
print("Type 'done' when you are finished adding stocks.")

my_stocks = {}   # stock name -> quantity

while True:
    name = input("\nStock name: ").upper()

    if name == "DONE":
        break

    if name not in prices:
        print("Sorry, I don't have a price for that stock.")
        continue

    qty = input("How many shares of " + name + "? ")

    if not qty.isdigit():
        print("That's not a valid number, try again.")
        continue

    qty = int(qty)

    # if the stock was already added, just add to it
    if name in my_stocks:
        my_stocks[name] = my_stocks[name] + qty
    else:
        my_stocks[name] = qty

# work out the total
total = 0
print("\n--- Your portfolio ---")
for name in my_stocks:
    value = my_stocks[name] * prices[name]
    total = total + value
    print(name, ":", my_stocks[name], "x", prices[name], "=", value)

print("Total investment:", total)

# ask if they want to save it to a file
save = input("\nSave this to a file? (y/n): ").lower()

if save == "y":
    file = open("portfolio.txt", "w")
    for name in my_stocks:
        value = my_stocks[name] * prices[name]
        file.write(name + ": " + str(my_stocks[name]) + " x " + str(prices[name]) + " = " + str(value) + "\n")
    file.write("Total investment: " + str(total) + "\n")
    file.close()
    print("Saved to portfolio.txt")
