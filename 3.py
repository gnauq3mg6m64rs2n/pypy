person = []

sum = 0
cnt = 0
with open("3.txt") as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        split = line.split(' ')
        if len(split) != 2:
            continue
        z = int(split[1])
        person.append({'f': split[0], 'z': z})
        sum += z
        cnt += 1

for p in person:
    if p['z'] < 20:
        print(p['f'])

print('avg {}'.format(sum / max(cnt, 1)))
