from math import ceil, log
import sys


def get_current_diff_payment(principal, interest, periods, current_payment):
    return ceil(principal / periods + interest * (principal - principal * (current_payment) / periods))


def get_credit_principal(interest, annuity, payments_number):
    return int(annuity / (interest * ((1 + interest) ** payments_number) / (((1 + interest) ** payments_number) - 1)))


def get_payments_number(interest, principal, annuity):
    return ceil(log(annuity / (annuity - interest * principal), 1 + interest))


def get_credit_interest(percentage):
    return (percentage / 100) / 12


def get_credit_annuity(interest, principal, periods):
    return ceil(
        principal * (interest * ((1 + interest) ** periods) / (((1 + interest) ** periods) - 1)))


def convert_to_years(months):
    return months // 12, months % 12


args = sys.argv
preped_args = args[1:5]
nums = '1234567890'

if len(args) != 5:
    print('Incorrect parameters')
    exit(0)

for i in range(4):
    preped_args[i] = preped_args[i][0:preped_args[i].find('=') + 1]

if '--type=' not in args[1]:
    print('Incorrect parameters')
    exit(0)

param_type = args[1].lstrip('--type=')

if param_type == 'annuity':

    if '--payment=' not in preped_args:
        principal = int(args[2].lstrip('--principal='))
        periods = int(args[3].lstrip('--periods='))
        interest = get_credit_interest(float(args[4].lstrip('--interest=')))

        annuity = get_credit_annuity(principal=principal, periods=periods, interest=interest)
        overpayment = periods * annuity - principal

        print(f'Your annuity payment = {annuity}!')
        print(f'Overpayment = {overpayment}')

    elif '--principal=' not in preped_args:
        payment = int(args[2].lstrip('--payment='))
        periods = int(args[3].lstrip('--periods='))
        interest = get_credit_interest(float(args[4].lstrip('--interest=')))

        principal = get_credit_principal(annuity=payment, payments_number=periods, interest=interest)
        overpayment = periods * payment - principal

        print(f'Your credit principal = {principal}!')
        print(f'Overpayment = {overpayment}')

    elif '--periods=' not in preped_args:
        principal = int(args[2].lstrip('--principal='))
        payment = int(args[3].lstrip('--payment='))
        interest = get_credit_interest(float(args[4].lstrip('--interest=')))

        periods = get_payments_number(principal=principal, annuity=payment, interest=interest)
        overpayment = periods * payment - principal

        periods = convert_to_years(periods)

        years = periods[0]
        months = periods[1]

        if years == 0:
            if months != 1:
                print(f'You need {months} months to repay this credit!')
            else:
                print(f'You need {months} month to repay this credit!')

        elif months == 0:
            if years != 1:
                print(f'You need {years} years to repay this credit!')
            else:
                print(f'You need {years} year to repay this credit!')

        else:
            if years > 0 and months > 0:
                print(f'You need {years} years and {months} months to repay this credit!')
            elif years > 0 and months == 1:
                print(f'You need {years} years and {months} month to repay this credit!')
            elif years == 1 and months > 0:
                print(f'You need {years} year and {months} months to repay this credit!')

        print(f'Overpayment = {overpayment}')

    else:
        print('Incorrect parameters')
        exit(0)

elif param_type == 'diff':

    if '--principal=' not in args[2]:
        print('Incorrect parameters')
        exit(0)

    if '--periods=' not in args[3]:
        print('Incorrect parameters')
        exit(0)

    if '--interest=' not in args[4]:
        print('Incorrect parameters')
        exit(0)

    principal = int(args[2].lstrip('--principal='))
    periods = int(args[3].lstrip('--periods='))
    interest = get_credit_interest(float(args[4].lstrip('--interest=')))

    _sum = 0
    current_payment = 0

    for i in range(periods):
        current_payment = get_current_diff_payment(principal=principal, interest=interest, periods=periods,
                                                   current_payment=i)
        print(f'Month{i + 1}: paid out {current_payment}')
        _sum += current_payment

    print('Overpayment = ' + str(_sum - principal))
else:
    print('Incorrect parameters')
    exit(0)
