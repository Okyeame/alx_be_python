monthly_income = int(input("enter your monthly income:")) 
total_monthly_expenses = int(input("Enter your total monthly expenses:")) 
monthly_savings = monthly_income - total_monthly_expenses
print ("Monthly savings is", monthly_savings)
projected_Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print ("Projected savings after one year, with interest is", projected_Savings)




