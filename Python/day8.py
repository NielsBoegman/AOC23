import sys

dirdict = {'R':1,'L':0}
mapdict = {}
def readInput():
    return open(sys.argv[1])

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)

def allz(keys):
    for key in keys:
        if not key[2] == 'Z':
            return False
    return True

def findLength(key,directions,p2):
    maxlen = len(directions)
    counter = 0
    while True:
        key = mapdict[key][dirdict[directions[counter%maxlen]]]
        counter += 1
        if p2 and key[2] == 'Z':
            return counter
        if not p2 and key == "ZZZ":
            return counter

def solve(f):
    directions = f.readline().strip()
    f.readline()
    akeys = []
    for line in f.readlines():
        key, value = line.split(' = ')
        value = value.strip()[1:-1].split(", ")
        mapdict[key] = value
        if key[2] == 'A':
            akeys.append(key)
    startkey = "AAA"
    p1 = findLength(startkey,directions,False)
    p2 = []
    for key in akeys:
        p2.append(findLength(key,directions,True))
    while not len(p2)==1:
        p2.append(lcm(p2[0], p2[1]))
        p2 = p2[2:]
    return([p1,p2[0]]) 

solutions = solve(readInput())
print("Part1: ", solutions[0])
print("Part2: ", solutions[1])