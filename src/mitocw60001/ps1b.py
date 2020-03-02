import numpy as np

annual_salary = float(input("Enter the starting annual salary: "))
portion_saved = float(input("Enter the portion of salary saved: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise: "))

# cost needed for a down payment (25% of total cost)
portion_down_payment = 0.25*total_cost
current_savings = 0
month_counter = 0
rate = 0.04

while current_savings <= portion_down_payment:
    current_savings += current_savings*rate/12
    current_savings += portion_saved*annual_salary/12
    month_counter += 1
    if month_counter % 6 == 0: annual_salary += annual_salary*semi_annual_raise

print("Number of months: {}, {} years".format(month_counter, month_counter/12))

