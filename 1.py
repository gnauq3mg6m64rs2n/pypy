import os

file1 = open("1.txt", "w")

while True:
    s = input()

    if s == '':
        break

    file1.write(s + os.linesep)

file1.close()
