with open("2.txt") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, len(line.split())))
        line = fp.readline()
        cnt += 1

print("Lines {}".format(cnt))
