shop = []

for i in range(1, 3):
    print('название')
    name = input()
    print('цена')
    price = input()
    print('количество')
    amount = input()

    shop.append((i, {'название': name, 'цена': price, 'количество': amount, 'eд': 'шт.'}))

stat = {}

for item in shop:
    item_ = item[1]

    for key in item_:
        val = item_[key]
        if key in stat:
            if val not in stat[key]:
                stat[key].append(val)
        else:
            stat[key] = []
            stat[key].append(val)

print(stat)
