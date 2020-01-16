n = int(input())

res = 0
while n > 0:
    n_ = n % 10
    res = max(res, n_)
    n = int(n / 10)

print(res)
