si = input()

count = 1
for s in si.split(' '):
    print(count, s[0:10])
    count = count + 1
