import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file_name = "expenses.csv"

try:
    df = pd.read_csv(file_name)
    df["Date"] = pd.to_datetime(df["Date"])
except:
    print("No file found. Creating new expense file...")
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(file_name, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    new_data = pd.DataFrame([[date, category, amount]],
                            columns=["Date", "Category", "Amount"])

    global df
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_name, index=False)

    print("Expense added successfully!\n")

def show_analysis():
    if df.empty:
        print("No data available.\n")
        return

    print("\n===== EXPENSE ANALYSIS =====")

    # Total spending
    total = df["Amount"].sum()
    print("Total Spending:", total)

    # Category-wise
    category = df.groupby("Category")["Amount"].sum()
    print("\nSpending by Category:")
    print(category)

    # Highest category
    print("\nHighest Spending Category:", category.idxmax())

    # Daily average
    daily_avg = df.groupby("Date")["Amount"].sum().mean()
    print("Average Daily Spending:", round(daily_avg, 2))

    # Suggestion
    if total > 3000:
        print("\n You are spending too much!")
    else:
        print("\n Spending is under control.")

    print()

def show_chart():
    if df.empty:
        print("No data to plot.\n")
        return

    category = df.groupby("Category")["Amount"].sum()

    category.plot(kind="bar")
    plt.title("Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("====== SMART EXPENSE ANALYZER ======")
        print("1. Add Expense")
        print("2. Show Analysis")
        print("3. Show Chart")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_analysis()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("Exiting... ")
            break
        else:
            print("Invalid choice\n")

# Run app
menu()