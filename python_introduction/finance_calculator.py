monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - total_monthly_expenses
annual_savings = monthly_savings * 12

projected_savings = annual_savings + (annual_savings * 0.05) #this is projected annual saving formulae

print("Your monthly savings are", "$" + str(monthly_savings))
print("projected savings after one year, with interest is:", "$" + str(projected_savings))