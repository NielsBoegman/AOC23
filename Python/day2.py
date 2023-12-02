import sys
import re
import numpy as np

def readInput():
    f = open(sys.argv[1])
    return f

def valid(rgb):
    if rgb[0]>12 or rgb[1]>13 or rgb[2]>14:
        return False
    return True
    
def count(line):
    maxrgb = [0,0,0]
    for i in range(len(line)):
        t = line[i].split(", ")
        rgb=[0,0,0]
        for j in t:
            temp = j.split()
            match temp[1]:
                case "red": rgb[0]+=int(temp[0])
                case "green": rgb[1]+=int(temp[0])
                case "blue": rgb[2]+=int(temp[0])
        maxrgb = [max(rgb[0],maxrgb[0]), max(rgb[1],maxrgb[1]), max(rgb[2],maxrgb[2])]
    return maxrgb

def parse(l):
    line = re.sub("Game \d*: ", "", l)
    line = re.sub("\n","",line)
    line = line.split("; ")
    counts = count(line)
    return [valid(counts), counts]

def solve(f):
    p1 = 0
    p2 = 0
    counter=1
    for line in f.readlines():
        results = parse(line)
        p1+=results[0]*counter
        p2+=np.prod(results[1])
        counter+=1
    return [p1,p2]

def part1(r):
    print("Part1: ", r[0])

def part2(r):
    print("Part2: ", r[1])

result = solve(readInput())
part1(result)
part2(result)