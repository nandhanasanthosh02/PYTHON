def add_expense():
    with open("expenses.txt", "a") as f:
        item = input("Enter item: ")
        amount = input("Enter amount: ")
        f.write(item + "," + amount + "\n")
    print("Expense added!\n")

def view_expenses():
    print("\n--- Expenses ---")
    total = 0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                item, amount = line.strip().split(",")
                print(f"{item}: {amount}")
                total += float(amount)
        print("Total Spent =", total, "\n")
    except FileNotFoundError:
        print("No expenses found!\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice!\n")
