import os

dict_ = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'четыре'}

with open("4.txt") as fp:
    file1 = open("4_out.txt", "w")
    line = fp.readline()
    while line:
        split = line.split(' — ')
        if len(split) != 2:
            continue
        val_ = dict_.get(split[0], split[0])
        file1.write(val_ + ' — ' + split[1] + os.linesep)
        line = fp.readline()
