import os

BANK_FILE = "bank_records.txt"

# Function to initialize the file
def initialize_file():
    if not os.path.exists(BANK_FILE):
        with open(BANK_FILE, "w") as f:
            f.write("AccountHolder,IFSC,Balance\n")


def create_account():
    name = input("Enter Account Holder Name: ")
    ifsc = input("Enter IFSC Code: ")
    balance = float(input("Enter Initial Balance: "))

    with open(BANK_FILE, "a") as f:
        f.write(f"{name},{ifsc},{balance}\n")
    print("✅ Account created successfully!")


def view_accounts():
    with open(BANK_FILE, "r") as f:
        print(f.read())


def search_account(name):
    with open(BANK_FILE, "r") as f:
        for line in f.readlines()[1:]:  
            acc_name, ifsc, balance = line.strip().split(",")
            if acc_name.lower() == name.lower():
                return acc_name, ifsc, float(balance)
    return None

def update_balance(name, new_balance):
    lines = []
    with open(BANK_FILE, "r") as f:
        lines = f.readlines()

    with open(BANK_FILE, "w") as f:
        for line in lines:
            if line.startswith(name + ","):
                parts = line.strip().split(",")
                parts[2] = str(new_balance)
                f.write(",".join(parts) + "\n")
            else:
                f.write(line)


def deposit():
    name = input("Enter Account Holder Name: ")
    account = search_account(name)
    if account:
        _, _, balance = account
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        update_balance(name, balance)
        print("✅ Deposit successful!")
    else:
        print("❌ Account not found.")


def withdraw():
    name = input("Enter Account Holder Name: ")
    account = search_account(name)
    if account:
        _, _, balance = account
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("❌ Insufficient balance!")
        else:
            balance -= amount
            update_balance(name, balance)
            print("✅ Withdrawal successful!")
    else:
        print("❌ Account not found.")


def main():
    initialize_file()
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("❌ Invalid choice! Try again.")


main()