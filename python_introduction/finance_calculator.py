monthly_income = int(input("enter your monthly income:")) 
total_monthly_expenses = int(input("Enter your total monthly expenses:")) 
difference_result = monthly_income - total_monthly_expenses
print ("Monthly savings is", difference_result)
annual_interest_rate = 5/100
projected_Savings = difference_result * 12
projected_mothly_savings_rate = difference_result * 12 * 0.05
annual_Savings_Projection_Calc = projected_Savings + projected_mothly_savings_rate
print ("projected annual savings is", annual_Savings_Projection_Calc)


