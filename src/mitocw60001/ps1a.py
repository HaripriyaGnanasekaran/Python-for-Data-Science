import numpy as np

annual_salary = float(input("Enter the starting annual salary: "))
portion_saved = float(input("Enter the portion of salary saved: "))
total_cost = float(input("Enter the cost of your dream house: "))

# cost needed for a down payment (25% of total cost)
portion_down_payment = 0.25*total_cost
current_savings = 0
month_counter = 0
rate = 0.04

while current_savings <= portion_down_payment:
    current_savings = current_savings + current_savings*rate/12
    current_savings += portion_saved*annual_salary/12
    month_counter += 1

print("It will take you " + str(month_counter) + " months, to save enough money")

