print('выручка')
pay_in = int(input())
print('издержки')
pay_out = int(input())
profit = pay_in / pay_out

if profit > 1:
    print('прибыль — выручка больше издержек')
    print('рентабельность {:.0%}'.format(profit))
    print('численность сотрудников')
    people_count = int(input())
    print('прибыль фирмы в расчете на одного сотрудника {:.0%}'.format(profit / people_count))
else:
    print('убыток — издержки больше выручки')

