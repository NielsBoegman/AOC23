import sys

def readInput():
    return open(sys.argv[1])

def checkColumn(pattern, col, p2):
    errors = 0
    for x in range(1, len(pattern[0])):
        if col -(x-1)<0 or col+x>=len(pattern[0]):
            if p2:
                return errors == 1
            return True
        for y in range(len(pattern)):
            if not pattern[y][col-(x-1)] == pattern[y][col+x]:
                errors+=1
                if not p2:
                    return False
    if p2:
        return errors==1
    return True
            
def checkRow(pattern, row, p2):
    errors = 0
    for x in range(1, len(pattern)):
        if row-(x-1)<0 or row+x>=len(pattern):
            if p2:
                return errors == 1
            return True
        for y in range(len(pattern[0])):
            if not pattern[row-(x-1)][y] == pattern[row+x][y]:
                errors+=1
                if not p2:
                    return False
    if p2:
        return errors == 1
    return True

def findReflection(pattern):
    result1 = 0
    result2 = 0
    for x in range(len(pattern[0])-1):
        if checkColumn(pattern, x, False):
            result1 += (x+1)
        if checkColumn(pattern, x, True):
            result2 += (x+1)
    for x in range(len(pattern)-1):
        if checkRow(pattern, x, False):
            result1 += (100*(x+1))
        if checkRow(pattern, x, True):
            result2+=(100*(x+1))
    return [result1,result2]

def solve(f):
    pattern = []
    res1 = 0
    res2 = 0
    for line in f.readlines():
        if line == "\n":
            res = findReflection(pattern)
            res1+= res[0]
            res2+=res[1]
            pattern = []
        else:
            pattern.append(list(line.strip()))
    res = findReflection(pattern)
    res1+=res[0]
    res2+=res[1]
    return [res1,res2]

solution = solve(readInput())
print("Part1: ", solution[0])
print("Part2: ", solution[1])