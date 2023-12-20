import sys

def readInput():
    return open(sys.argv[1])

def solve(f):
    map = []
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
        map.append(l)
        if empty:
            map.append(l)