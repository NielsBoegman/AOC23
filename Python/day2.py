import sys
import re

def readInput():
    f = open(sys.argv[1])
    return f.readlines()

def valid(rgb):
    if rgb[0]>12 or rgb[1]>13 or rgb[2]>14:
        return False
    return True
    

def count(line):
    maxr = 0
    maxb = 0
    maxg = 0
    for i in range(len(line)):
        t = line[i].split(", ")
        r=0
        b=0
        g=0
        for j in t:
            temp = j.split(" ")
            match temp[1]:
                case "red": r+=int(temp[0])
                case "blue": b+=int(temp[0])
                case "green": g+=int(temp[0])
        maxr=max(r, maxr)
        maxg=max(g,maxg)
        maxb=max(b,maxb)
    return [maxr,maxg,maxb]

def parse(l):
    p1 = 0
    p2 = 0
    for x in range(len(l)):
        line = re.sub("Game \d*: ", "", l[x])
        line = re.sub("\n","",line)
        line = line.split("; ")
        counts = count(line)
        if valid(counts):
            p1+=x+1
        p2+=counts[0]*counts[1]*counts[2]
    return [p1,p2]

def part1(r):
    print("Part1: ", r[0])

def part2(r):
    print("Part2: ", r[1])

result = parse(readInput())
part1(result)
part2(result)