import math

def i_nominal(i):
    return (i / 100) / (12 * 1)

def loan_principal(a, n, i):
    p = a / ((i_nominal(i) * (1 + i_nominal(i)) ** n) / ((1 + i_nominal(i)) ** n - 1))
    print(f"Your loan principal = {int(p)}!")

def n_payments(a, p, i):
    n = math.ceil(math.log((a / (a - i_nominal(i) * p)), 1 + i_nominal(i)))
    n_years = math.ceil(n / 12)
    
    if n % 12 == 0:
        print(f"It will take {n / 12} years to repay this loan!")
    
    elif n / 12 < 1:
        print(f"It will take {n % 12} months to repay this loan!")

    else:
        print(f"It will take {n // 12} years and {n % 12} months to repay this loan!")

def monthly_payment(p, n, i):
    a_monthly = p * ((i_nominal(i) * (1 + i_nominal(i)) ** n) / ((1 + i_nominal(i)) ** n -1)) 
    print(f"Your monthly payment = {math.ceil(a_monthly)}!")

def usr_n():
    p = float(input("Enter the loan principal:\n"))
    a = int(input("Enter the monthly payment:\n"))
    i = float(input("Enter the loan interest:\n"))
    return n_payments(a, p, i)

def usr_a():
    p = float(input("Enter the loan principal:\n"))
    n = int(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n"))
    return monthly_payment(p, n, i)

def usr_p():
    a = float(input("Enter the annuity payment:\n"))
    n = int(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n"))
    return loan_principal(a, n, i)


def menu():
    usr_option = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount, 
type "p" for loan principal:
''')
    
    if usr_option == "n":
        return usr_n()
    
    if usr_option == "a":
        return usr_a()
    
    if usr_option == "p":
        return usr_p()

menu()
