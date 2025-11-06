import matplotlib.pyplot as plt
import pandas as pd

def expensesTracker():
    filename = "data.csv"
    try:
        with open(filename, "x") as f:
            f.write("food,travel,shopping_bills,vegetables\n")
    except FileExistsError:
        pass

    food = int(input("Enter your food expenses: "))
    travel = int(input("Enter your travel expenses: "))
    shopping_bills = int(input("Enter your shopping expenses: "))
    vegetables = int(input("Enter your vegetables expenses: "))

    with open(filename,"a") as f:
        f.write(f"{food},{travel},{shopping_bills},{vegetables}\n")

    user = input("Do youy want to see your history (yes/no)")
    if user.lower() == "yes":
        with open(filename,"r") as f:
            history = f.read()
            print(history)

    df = pd.read_csv("data.csv")
    sums = df.sum()
    plt.figure(figsize=(5,5))
    plt.bar(sums.index, sums.values, color=['orange', 'purple', 'green', 'red'])
    plt.title("Total Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spent")
    plt.tight_layout()
    plt.show()        


expensesTracker()
