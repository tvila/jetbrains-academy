"""
Description
If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.

In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

payment = \dfrac{principal}{months}=\dfrac{1000}{9} =111.11...payment= 
months
principal
​	
 = 
9
1000
​	
 =111.11...

Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104lastpayment=principal−(periods−1)∗payment=1000−8∗112=104

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

Objectives
The behavior of your program should look like this:

Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
To perform further calculations, you'll also have to ask for the required missing value.
Finally, output the results for the user.
"""

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
