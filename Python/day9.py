import sys

def readInput():
    return open(sys.argv[1])

def solve(f):
    result = 0
    result2 = 0
    for line in f.readlines():
        temp = list(map(int, line.split()))
        result += findSequence(temp)
        temp.reverse()
        result2 += findSequence(temp)
    return [result,result2]

def allZero(l):
    for element in l:
        if not element == 0:
            return False
    return True

def findSequence(start):
    if allZero(start):
        return 0
    new = []
    for x in range(len(start)-1):
        new.append(start[x+1]-start[x])
    return start[-1] + findSequence(new)

solution = solve(readInput()) 
print("Part1: ", solution[0])
print("Part2: ", solution[1])