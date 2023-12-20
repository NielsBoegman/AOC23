import sys

def readInput():
    return open(sys.argv[1])

def solve(f):
    platform = []
    for line in f.readlines():
        platform.append(list(line.strip()))
    res1 = 0
    for x in range(len(platform[0])):
        start = len(platform)
        count = 0
        for y in range(len(platform)):
            if platform[y][x] == "#":
                start = len(platform) - y - 1
                count = 0
            if platform[y][x] == "O":
                res1+=start-count
                count+=1
    return [res1, 0]

result = solve(readInput())
print("Part1: ", result[0])