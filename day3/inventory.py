# Pharmacy Inventory Tracker
# CodeOps - Module 1, Day 3 mini-project

stock = {}

# 1. Load stock from file (safely, in case the file doesn't exist yet)
try:
    with open("stock.txt") as f:
        for line in f:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)
except FileNotFoundError:
    print("No stock file yet — starting empty")


# 2. Function to increase or decrease an item's quantity
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount


# 3. Function to show low-stock items (quantity under 10)
def show_low_stock():
    low = [item for item, qty in stock.items() if qty < 10]
    if low:
        print("Low stock:", low)
    else:
        print("Nothing is low on stock right now.")


# 4. Function to save the current stock back to the file
def save_stock():
    with open("stock.txt", "w") as f:
        for item, qty in stock.items():
            f.write(f"{item},{qty}\n")
    print("Stock saved.")


# 5. A simple menu so you can actually use the program
def main():
    while True:
        print("\n--- Pharmacy Inventory ---")
        for item, qty in stock.items():
            print(f"  {item}: {qty}")

        print("\n1. Adjust an item's quantity")
        print("2. Show low stock items")
        print("3. Save and quit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Item name: ")
            try:
                amount = int(input("Amount (use a negative number to remove stock): "))
                adjust(item, amount)
            except ValueError:
                print("Please enter a whole number.")
        elif choice == "2":
            show_low_stock()
        elif choice == "3":
            save_stock()
            break
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()