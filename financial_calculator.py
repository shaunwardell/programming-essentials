# Financial Calculator
# Programming Essentials

def get_income():
    while True:
        try:
            monthly_income = float(input("What is your monthly income? "))

            if monthly_income <= 0:
                print("Income must be greater than zero. Please try again.")
                continue

            return monthly_income

        except ValueError:
            print("Invalid input. Please enter your income as a number.")


def get_expenses():
    while True:
        try:
            monthly_expenses = float(input("What are your monthly expenses? "))
            return monthly_expenses

        except ValueError:
            print("Invalid input. Please enter your expenses as a number.")


def calculate_balance(income, expenses):
    balance = income - expenses
    return balance


def calculate_expense_percentage(income, expenses):
    percentage = (expenses / income) * 100
    return percentage


def analyze_expenses(percentage):
    if percentage > 80:
        print("Warning: Your expenses are very high compared to your income.")
    elif percentage > 60:
        print("Caution: A large portion of your income is going toward expenses.")
    else:
        print("Good: Your expenses are at a manageable percentage of your income.")


monthly_income = get_income()
monthly_expenses = get_expenses()

money_remaining = calculate_balance(monthly_income, monthly_expenses)
expense_percentage = calculate_expense_percentage(
    monthly_income, monthly_expenses
)

print(f"You have ${money_remaining:,.2f} remaining each month.")
print(f"Your expenses use {expense_percentage:.1f}% of your monthly income.")

analyze_expenses(expense_percentage)
        



