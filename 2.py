a = input()
b = input()
c = input()

l = [a, b, c]

tmp = l[0]
l[0] = l[1]
l[1] = tmp
l[2] = l[2]
