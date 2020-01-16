print('a')
a = int(input())
print('b')
b = int(input())

day_count = 1

while a < b:
    print('%d-й день: %5.2f' % (day_count, a))
    a = a * 1.1
    day_count = day_count + 1

print('%d-й день: %5.2f' % (day_count, a))
print('на %d-й день спортсмен достиг результата — не менее %d км.' % (day_count, b))
