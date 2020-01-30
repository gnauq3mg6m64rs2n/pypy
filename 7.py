avg_ = 0
cnt_ = 0

result = []
dict_f_ = {}

with open("7.txt") as fp:
    line = fp.readline()
    while line:
        split = line.split(' ')
        if len(split) != 4:
            continue
        print(split)
        p_ = int(split[2])
        s_ = int(split[3])
        profit = p_ - s_
        if profit > 0:
            avg_ += profit
            cnt_ += 1
        dict_f_[split[0]] = profit
        line = fp.readline()

result.append(dict_f_)
result.append({'average_profit': avg_ / max(cnt_, 1)})

print(result)
