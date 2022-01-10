import math
import argparse


def i_nominal(i):
    return (i / 100) / (12 * 1)


def diff_payment(p, n, i):
    m = 0
    total_pay = -p

    for j in range(n):
        m += 1
        dm = math.ceil(p / n + i_nominal(i) * (p - ((p * (m - 1) / n))))
        total_pay += dm
        print(f'Month {m}: payment is {dm}')

    print("")
    print(f'Overpayment = {total_pay}')


def repay(p, a, i):
    n = math.ceil(math.log((a / (a - i_nominal(i) * p)), 1 + i_nominal(i)))
    # n_years = math.ceil(n / 12)
    over_pay = math.ceil(n * a - p)

    if n % 12 == 0:
        print(f"It will take {int(n / 12)} years to repay this loan!")

    elif n / 12 < 1:
        print(f"It will take {n % 12} months to repay this loan!")

    else:
        print(f"It will take {n // 12} years and {n % 12} months to repay this loan!")

    print(f'Overpayment = {over_pay}')


def loan_principal(a, n, i):
    p = a / ((i_nominal(i) * (1 + i_nominal(i)) ** n) / ((1 + i_nominal(i)) ** n - 1))
    over_pay = math.ceil((a * n - p))
    print(f"Your loan principal = {int(p)}!")
    print(f"Overpayment = {over_pay}")


def monthly_payment(p, n, i):
    a_monthly = math.ceil(p * ((i_nominal(i) * (1 + i_nominal(i)) ** n) / ((1 + i_nominal(i)) ** n - 1)))
    print(f"Your annuity payment = {a_monthly}!")
    over_pay = (a_monthly * n - p)
    print(f'Overpayment = {math.ceil(over_pay)}')


#Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], help="write what kind of operation want to execute: Annuity or diff")
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()

# logic Argparse
if args.type == "annuity":
    if args.interest is None:
        print("Incorrect parameters")
    elif args.principal and args.periods and args.interest > 0:
        monthly_payment(args.principal, args.periods, args.interest)
    elif args.payment and args.periods and args.interest > 0:
        loan_principal(args.payment, args.periods, args.interest)
    elif args.principal and args.payment and args.interest > 0:
        repay(args.principal, args.payment, args.interest)
    else:
        print("Incorrect parameters")

elif args.type == "diff":
    if args.interest is None:
        print("Incorrect parameters")
    elif args.principal and args.periods and args.interest > 0:
        diff_payment(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
