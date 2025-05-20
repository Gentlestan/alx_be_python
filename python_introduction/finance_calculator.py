user_monthly_income = int(input("Enter your monthly income:"))
user_total_monthly_expenses = int(input("Enter your total monthly expenses:"))

user_monthly_saving = user_monthly_income - user_total_monthly_expenses

simple_annual_interest = 0.05

projected_savings = user_monthly_income * 12 + (user_monthly_saving * 12 * simple_annual_interest) #this is projected annual saving formulae

print("Your monthly savings are", "$" + str(user_monthly_saving))
print("projected savings after one year, with interest is:", "$" + str(projected_savings))