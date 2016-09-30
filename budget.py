# Budget Analysis Program
# Ask user for budget and monthly expenses

budget = float(input('Enter the amount of money you have budgeted for this month: $'))

total = 0
expense = float(input('Enter an expense or enter 0 to end: $'))

while expense != 0:
    total += expense
    expense = float(input('Enter an expense or enter 0 to end: $'))

print('Your total spent for the month is $',
      format(total, ',.2f'),
      sep='')

under = budget - total
over = total - budget

if total <= budget:
    print('You are', ('$' + format(under, ',.2f')), 'under budget.')
else:
    print('You are', ('$' + format(over, ',.2f')), 'over budget.')