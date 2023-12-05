import sys
import math

def readInput():
    if len(sys.argv)==1:
        print("Missing parameter, use the program like this: python3 day2.py [inputfile]")
        exit()
    try:
        f = open(sys.argv[1])
    except FileNotFoundError:
        print("File not found, check your filename and path and try again.")
        exit()
    return f

def updateRanges(s,m):
    res = []
    se = s
    while not se == []:
        temp = se[0]
        for ma in m:
            if ma[2] <= temp[0] and ma[3] >= temp[0]:
                if temp[1] <= ma[3]:
                    thing = [ma[0]+temp[0]-ma[2], ma[1]+temp[1]-ma[3]]
                    res.append(thing)
                    se = se[1:]
                    break
                else:  
                    se.append([ma[3]+1, temp[1]])
                    thing = [ma[3]+1, temp[1]]
                    temp = [temp[0],ma[3]]
                    res.append([ma[0]+temp[0]-ma[2], ma[1]+temp[1]-ma[3]])
                    se = se[1:]
                    break
            elif temp[1] >= ma[2] and temp[1] <= ma[3]: 
                se.append([temp[0], ma[2]-1])
                temp = [ma[2], temp[1]]
                thing = [[temp[0], ma[2]-1]]
                res.append([ma[0]+temp[0]-ma[2], ma[1]+temp[1]-ma[3]])
                se = se[1:]
                break
            elif temp[0] < ma[2] and temp[1] > ma[3]:
                se.append([temp[0], ma[2]-1])
                se.append([ma[2]+1, temp[1]])
                res.append([ma[0],ma[1]])
                se = se[1:]
                break
        if len(se)> 0 and temp == se[0]:
            res.append(temp)
            se=se[1:]
    return res
        


def part2(seeds, maps):
    s= []
    result = math.inf
    for x in range(1,len(seeds),2):
        s.append([seeds[x-1],seeds[x-1]+seeds[x]-1])
    for m in maps:
        s = updateRanges(s, m)
    for se in s:
        result = min(result, se[0])
    return result


def parseInput(f):
    maps = []
    seeds = []
    temp = []
    for line in f.readlines():
        if line == "\n":
            if temp == []:
                continue
            maps.append(temp)
            temp = []
            continue
        l = line.split()
        if l[0] == "seeds:":
            for x in l[1:]:
                seeds.append(int(x))
            continue
        if not l[0].isdigit():
            continue
        for i in range(len(l)):
            l[i] = int(l[i])
        temp.append([l[0],l[0]+l[2]-1, l[1],l[1]+l[2]-1])
    maps.append(temp)
    return seeds, maps

def findNumber(num, maps):
    for map in maps:
        if num>=map[2] and num<=map[3]:
            return(map[0] + num-map[2])
    return num

def solve(seeds, maps):
    location = math.inf
    for seed in seeds:
        val = seed
        for m in maps:
            val = findNumber(val, m)
        location = min(location, val)
    return location

seeds, maps = parseInput(readInput())
print("Part1: ", solve(seeds, maps))
print("Part2: ", part2(seeds, maps))