import math

principal = int(input('Enter the loan principal:\n'))

option = input('What do you want to calculate?\ntype "m" - for number of monthly payments,\ntype "p" - for the monthly payment:\n')

if option == "m":
    monthly_payment = int(input('Enter monthly payment:\n'))
    payments_calc = int(round(principal / monthly_payment, 0))

    if payments_calc != 1:
        print(f"It will take {payments_calc} months to repay the loan")
    else:
        print(f"It will take {payments_calc} month to repay the loan")

if option == "p":
    months = int(input("Enter the number of months:\n"))
    monthly_amount = math.ceil(principal / months)
    lastpayment = principal - (months - 1) * monthly_amount
    
    if monthly_amount != lastpayment:
        print(f'Your monthly payment = {monthly_amount} and the last payment = {lastpayment}.')
              
    else:
        print(f'Your monthly payment = {monthly_amount}')
    
