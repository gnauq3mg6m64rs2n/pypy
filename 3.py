m = int(input())

if m < 1 or m > 12:
    print('виде целого числа от 1 до 12')

d = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
     10: 'осень', 11: 'осень'}

print(d[m])
