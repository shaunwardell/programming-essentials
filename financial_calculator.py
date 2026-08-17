# Financial Calculator
# Programming Essentials

monthly_income = float(input("What is your monthly income? "))
monthly_expenses = float(input("What are your monthly expenses? "))

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
