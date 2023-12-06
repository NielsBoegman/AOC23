import sys

def readInput():
    return open(sys.argv[1]).readlines()

def part1(lines):
    res = 1
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))
    for x in range(len(times)):
        temp = 0
        for z in range(times[x]):
            if (times[x]-z)*z > distances[x]:
                temp=z
                break
        res *= times[x]-2*temp + 1
    return res

def part2(lines):
    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))
    start = 0
    for x in range(time):
        if (time - x) * x > distance:
            start = x
            break
    return (time-2*start)
    
l = readInput()
print("Part1: ",part1(l))
print("Part2: ", part2(l))