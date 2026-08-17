# Financial Calculator
# Programming Essentials

while True:
    try:
        monthly_income = float(input("What is your monthly income? "))

        if monthly_income <= 0:
            print("Income must be greater than zero. Please try again.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter your income as a number.")
while True:
    try:
        monthly_expenses = float(input("What are your monthly expenses? "))
        break
    except ValueError:
        print("Invalid input. Please enter your expenses as a number.")
money_remaining = monthly_income - monthly_expenses

print(f"You have ${money_remaining:,.2f} remaining each month.")
money_remaining = monthly_income - monthly_expenses
expense_percentage = (monthly_expenses / monthly_income) * 100
print(f"Your expenses use {expense_percentage:.1f}% of your monthly income.")
if expense_percentage > 80:
    print("Warning: Your expenses are very high compared to your income.")
elif expense_percentage > 60:
    print("Caution: A large portion of your income is going toward expenses.")
else:
    print("Good: Your expenses are at a manageable percentage of your income.")

