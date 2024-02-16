#Get user input, ask for needed info
annual_salary = input("Enter your annual salary: ")
annual_salary = int(annual_salary) #str -> int

portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved) #str -> float

total_cost = input("Enter the cost of your dream home: ")
total_cost = int(total_cost) #str -> int

semi_annual_raise = input("Enter the semi­annual raise, as a decimal: ")
semi_annual_raise = float(semi_annual_raise)

#Value Initialization
portion_down_payment = 0.25
r = 0.04

#Math
down_payment = portion_down_payment * total_cost

#Savings
current_savings = 0.0
months = 0
monthly_salary = annual_salary / 12
while current_savings < down_payment:
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    months+=1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

print("Number of months: " + str(months))