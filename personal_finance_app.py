from datetime import datetime

# List to store all transactions
all_records = []

# Function to add income
def add_income():
    amount = float(input("Enter the income amount: "))
    source = input("Enter the income source (for example: salary, freelance): ")
    note = input("Add a note (optional): ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    income_record = {
        "type": "income",
        "amount": amount,
        "category": source,
        "note": note,
        "date": date_time
    }
    all_records.append(income_record)
    print("Income has been added.\n")

# Function to add expense
def add_expense():
    amount = float(input("Enter the expense amount: "))
    reason = input("Enter the expense reason (for example: rent, food): ")
    note = input("Add a note (optional): ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense_record = {
        "type": "expense",
        "amount": amount,
        "category": reason,
        "note": note,
        "date": date_time
    }
    all_records.append(expense_record)
    print("Expense has been added.\n")

# Function to show balance
def show_balance():
    total_income = sum(item["amount"] for item in all_records if item["type"] == "income")
    total_expense = sum(item["amount"] for item in all_records if item["type"] == "expense")
    current_balance = total_income - total_expense

    print(f"\nTotal Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Current Balance: {current_balance}\n")

# Function to show all transactions
def show_transactions():
    if not all_records:
        print("There are no transactions to show.\n")
        return

    print("\nTransaction History:")
    for record in all_records:
        print(f"{record['date']} | {record['type']} | {record['amount']} | {record['category']} | {record['note']}")
    print()

# Main menu
def main():
    while True:
        print("Personal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show All Transactions")
        print("5. Exit")

        user_choice = input("Enter your choice (1 to 5): ")

        if user_choice == "1":
            add_income()
        elif user_choice == "2":
            add_expense()
        elif user_choice == "3":
            show_balance()
        elif user_choice == "4":
            show_transactions()
        elif user_choice == "5":
            print("Thank you for using the finance manager.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the app
if __name__ == "__main__":
    main()
