import sys

def readInput():
    return open(sys.argv[1])

def solve(f):
    stars = []
    count = 0
    for line in f.readlines():
        l = []
        empty = True
        for x in line:
            if x == '.':
                l.append(x)
                empty = False
            elif x =='#':
                l.append(chr(count))
                count+=1
            else: continue
        stars.append(l)
        if empty:
            stars.append(l)
    for x in range(len(stars[0])):
        empty = True
        for y in range(len(stars)):
            if stars[x][y].isdigit():
                empty = False