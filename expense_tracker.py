# Personal Expense Tracker

expenses = []
monthly_budget = 0

data_file = "expense_data.csv"

categories = ["Food", "Travel", "Rent", "Studies", "Other"]

def load_data():
    global monthly_budget
    expenses.clear()
    try:
        f = open(data_file, "r")
        lines = f.readlines()
        f.close()

        if len(lines) < 4:
            return

        monthly_budget = float(lines[1].split(",")[1])

        for line in lines[4:]:
            if line.startswith("DATE"):
                continue
            d, c, a, desc = line.strip().split(",")
            expenses.append({
                "date": d,
                "category": c,
                "amount": float(a),
                "description": desc
            })
    except:
        pass

def save_data():
    total = 0
    for e in expenses:
        total += e["amount"]

    remaining = monthly_budget - total

    f = open(data_file, "w")
    f.write("TYPE,VALUE,EXTRA1,EXTRA2\n")
    f.write("BUDGET," + str(monthly_budget) + ",0,0\n")
    f.write("REMAINING," + str(remaining) + ",0,0\n")
    f.write("DATE,CATEGORY,AMOUNT,DESCRIPTION\n")

    for e in expenses:
        f.write(
            e["date"] + "," +
            e["category"] + "," +
            str(e["amount"]) + "," +
            e["description"] + "\n"
        )
    f.close()

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")

    print("Select category:")
    for i in range(len(categories)):
        print(i + 1, categories[i])

    choice = int(input("Enter category number: "))
    category = categories[choice - 1]

    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })

    save_data()

def view_expenses():
    if not expenses:
        print("No expenses found")
        return

    for e in expenses:
        print(e["date"], "|", e["category"], "|", e["amount"], "|", e["description"])

def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter monthly budget: "))
    save_data()

def view_month_expenses():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    print("Expenses for", month)
    for e in expenses:
        if e["date"].startswith(month):
            print(e["date"], "|", e["category"], "|", e["amount"], "|", e["description"])
            total += e["amount"]

    print("Total spending:", total)
    print("Money left:", monthly_budget - total)

load_data()

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Set Monthly Budget")
    print("4. View Monthly Expenses")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        set_budget()
    elif ch == "4":
        view_month_expenses()
    elif ch == "5":
        break
    else:
        print("Invalid choice")
