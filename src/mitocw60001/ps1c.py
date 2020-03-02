import numpy as np

annual_salary = float(input("Enter the starting annual salary: "))

total_cost = 500000
semi_annual_raise = .07

# cost needed for a down payment (25% of total cost)
portion_down_payment = 0.25*total_cost
current_savings = 0
months = 36
rate = 0.04


def target_function (portion_saved,current_savings,rate,annual_salary,semi_annual_raise, portion_down_payment,months):
    for month in range(months):
        current_savings += current_savings*rate/12
        current_savings += portion_saved*annual_salary/12
        if month % 6 == 0: annual_salary += annual_salary*semi_annual_raise
    return portion_down_payment-current_savings;

# bisection search
a = 1
b = 0
c = (a+b)/2

count = 0
while (abs(c-a) > 0.0001 and count < 20):
    count+=1
    fa =  target_function (a,current_savings,rate,annual_salary,semi_annual_raise, portion_down_payment,months)
    fb =  target_function (b,current_savings,rate,annual_salary,semi_annual_raise, portion_down_payment,months)
    c = (a+b)/2
    if (np.sign(fa) > 0 and np.sign(fb) <0):
        temp = (a+b)/2
        fc =  target_function (temp,current_savings,rate,annual_salary,semi_annual_raise, portion_down_payment,months)
        if (np.sign(fc) < 0):
            b = temp
            c = (a+b)/2
        else:
            a = temp
            c = (a+b)/2
    elif (np.sign(fa) < 0 and np.sign(fb) > 0):
        temp = (a+b)/2
        fc =  target_function (temp,current_savings,rate,annual_salary,semi_annual_raise, portion_down_payment,months)
        if (np.sign(fc) < 0):
            a = temp
            c = (a+b)/2
        else:
            b = temp
            c = (a+b)/2
    else: 
        pass

if count<20:
    print("Best savings rate: {}".format(c))
    print("Steps in bisection search: {}".format(count))
else:
    print("It is not possible to pay the down payment in three years.")

