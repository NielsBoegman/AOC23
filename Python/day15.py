import sys

def readInput():
    return open(sys.argv[1])

def hash(key):
    cv = 0
    for x in key:
        cv += ord(x)
        cv *= 17
        cv = cv%256
    return cv

def solve(f):
    res1 = 0
    for x in f.readline().split(","):
        temp = hash(x)
        res1 += temp
    return [res1,0]

result = solve(readInput())
print("Part1: ", result[0])
