#Get user input, ask for needed info
annual_salary = input("Enter your annual salary: ")
annual_salary = int(annual_salary) #str -> int

portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved) #str -> float

total_cost = input("Enter the cost of your dream home: ")
total_cost = int(total_cost) #str -> int

#Value Initialization
portion_down_payment = 0.25
r = 0.04

#Math
down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12

#Savings
current_savings = 0.0
months = 0
while current_savings < down_payment:
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    months+=1

print("Number of months: " + str(months))