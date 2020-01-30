import random

file1 = open("5_out.txt", "w")

for i in range(5):
    file1.write(str(random.randint(0, 100)) + ' ')

file1.close()

with open("5_out.txt") as fp:
    sum_ = 0
    line = fp.readline()
    while line:
        split = line.split(' ')
        if len(split) == 0:
            continue

        for i in split:
            if len(i) == 0:
                continue
            sum_ += int(i)

        line = fp.readline()

    print(sum_)
