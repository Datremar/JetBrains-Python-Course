from math import ceil, log


def get_credit_interest(percentage):
    return (percentage / 100) / 12


def get_payments_number(interest, principal, annuity):
    interest = get_credit_interest(interest)
    return ceil(log(annuity / (annuity - interest * principal), 1 + interest))


def get_credit_principal(interest, annuity, payments_number):
    interest = get_credit_interest(interest)
    return int(annuity / (interest * ((1 + interest) ** payments_number) / (((1 + interest) ** payments_number) - 1)))


def get_credit_annuity(interest, principal, payments_number):
    interest = get_credit_interest(interest)
    return ceil(principal * (interest * ((1 + interest) ** payments_number) / (((1 + interest) ** payments_number) - 1)))


def convert_to_years(months):
    return months // 12, months % 12


print('What do you want to calculate? ')
print('type "n" - for count of months, \ntype "a" - for annuity monthly payment, \ntype "p" - for monthly payment: ')

calculation_configuration = input().lstrip('> ')

if calculation_configuration == 'n':
    print('Enter credit principal: ')
    credit_principal = int(input().lstrip('> '))

    print('Enter monthly payment: ')
    monthly_payment = int(input().lstrip('> '))

    print('Enter credit interest: ')
    interest = float(input().lstrip('> '))

    result = convert_to_years(get_payments_number(principal=credit_principal, annuity=monthly_payment, interest=interest))

    years = result[0]
    months = result[1]

    if years == 0:
        if months != 1:
            print(f'{months} months to repay this credit!')
        else:
            print(f'{months} month to repay this credit!')

    elif months == 0:
        if years != 1:
            print(f'{years} years to repay this credit!')
        else:
            print(f'{years} year to repay this credit!')

    else:
        if years > 0 and months > 0:
            print(f'{years} years and {months} months to repay this credit!')
        elif years > 0 and months == 1:
            print(f'{years} years and {months} month to repay this credit!')
        elif years == 1 and months > 0:
            print(f'{years} year and {months} months to repay this credit!')

elif calculation_configuration == 'p':
    print('Enter monthly payment: ')
    monthly_payment = float(input().lstrip('> '))

    print('Enter count of periods: ')
    months_count = int(input().lstrip('> '))

    print('Enter credit interest: ')
    interest = float(input().lstrip('> '))

    principal = get_credit_principal(annuity=monthly_payment, payments_number=months_count, interest=interest)

    print(f'Your credit principal = {principal}!')

elif calculation_configuration == 'a':
    print('Enter the credit principal: ')
    credit_principal = int(input().lstrip('> '))

    print('Enter count of periods: ')
    months_count = int(input().lstrip('> '))

    print('Enter credit interest: ')
    interest = float(input().lstrip('> '))

    annuity = get_credit_annuity(principal=credit_principal, payments_number=months_count, interest=interest)

    print(f'Your annuity payment = {annuity}!')
