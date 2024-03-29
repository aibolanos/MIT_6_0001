#Savings Method
def savings(starting_salary, portion_saved):
    current_savings = 0
    monthly_salary = starting_salary / 12
    for x in range(36):
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved
        if (x+1) % 6 == 0:
            starting_salary += starting_salary * semi_annual_raise
            monthly_salary = starting_salary / 12
    return current_savings

#Get user input, ask for needed info
starting_salary = input("Enter the starting salary: ")
starting_salary = int(starting_salary) #str -> int

#Value Initialization
semi_annual_raise = 0.07
r = 0.04 #apr
portion_down_payment = 0.25
total_cost = 1000000
epsilon = 100 #Our Savings can be in the range of $100 of Down Payment

#Math
down_payment = portion_down_payment * total_cost

#Bisection Search
steps = 0
high = 10000
low = 0
guess = (high + low) / 2
while True:
    if savings(starting_salary, 1) < down_payment:
        print("It is not possible to pay the down payment in three years.")
        break
    rate = down_payment - savings(starting_salary, round(guess/10000, 4))
    if  abs(rate) > epsilon:
        if down_payment - savings(starting_salary, round(guess/10000, 4)) > epsilon:
            low = guess
        else:
            high = guess
        guess = (high+low)/2
        steps+=1
    else:
        print("Best savings rate: " + str(round(guess/10000, 4)))
        print("Steps in bisection search: " + str(steps))
        break
