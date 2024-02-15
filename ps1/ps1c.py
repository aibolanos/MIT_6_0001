# portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
# portion_saved = float(portion_saved) #str -> float



#Get user input, ask for needed info
starting_salary = input("Enter the starting salary: ")
starting_salary = int(starting_salary) #str -> int

#Value Initialization
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000

#Math
down_payment = portion_down_payment * total_cost
#time is 36 months
#looking for an integer SAVINGS rate>

#Savings
def savings(starting_salary, portion_saved):
    # print("Salary: " + str(starting_salary))
    # print("Portion Saved: " + str(portion_saved))
    current_savings = 0.0
    # print("Current Savings: " + str(current_savings))
    months = 0
    # print("Months: " + str(months))
    # print("START LOOP")
    for x in range(36):
        current_savings += current_savings * (r / 12)
        # print("IL Current Savings return: " + str(x) + " " + str(current_savings))
        monthly_salary = starting_salary / 12
        # print("IL Monthly Salary: " + str(x) + " " +str(monthly_salary))
        current_savings += monthly_salary * (portion_saved / 10000)
        # print("IL Current Savings New Month: " + str(x) + " " + str(current_savings))
        # print(" Ending Month " + str(months) + " with " + str(current_savings) + " savings and " + str(monthly_salary))
        months+=1
        if months % 6 == 0:
            starting_salary += starting_salary * semi_annual_raise
    # print("END LOOP")
    return current_savings

#Bisection Search
steps = 0
high = 10000
low = 0
guess = (high + low) / 2

while savings(starting_salary, guess) > down_payment + 100 or savings(starting_salary, guess) < down_payment - 100:
    print("High: " + str(high)+ " Low: " + str(low) + " Guess: " + str(guess/10000))
    # print("Savings: " + str(savings(starting_salary, guess)))
    if savings(starting_salary, guess) < down_payment - 100:
        #print(savings(starting_salary, guess) < down_payment - 100)
        print("Too Low!")
        low = guess
    else:
        print("Too High!")
        high = guess
    guess = (high+low)/2
    steps+=1

#return
print("Best savings rate: " + str(round(guess/10000, 4)))
print("Steps in bisection search: " + str(steps))