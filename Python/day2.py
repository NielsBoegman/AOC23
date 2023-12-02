import sys
import re

def readInput():
    f = open(sys.argv[1])
    return f.readlines()

def solve(l):
    p1 = 0
    p2 = 0
    for x in range(len(l)):
        line = re.sub("Game \d*: ", "", l[x])
        line = re.sub("\n","",line)
        line = line.split("; ")
        valid = True
        gr = 0
        gb = 0
        gg = 0
        for i in range(len(line)):
            temp = line[i].split(", ")
            rc = 0
            bc = 0
            gc = 0
            for z in temp:
                t = z.split(" ")
                match t[1]:
                    case "red": rc+= int(t[0])
                    case "blue": bc+= int(t[0])
                    case "green": gc+= int(t[0])
            if rc>12 or gc>13 or bc>14:
                valid = False
            if rc > gr:
                gr = rc
            if bc > gb:
                gb = bc
            if gc > gg:
                gg = gc
        p2+=(gg*gb*gr) 
        if valid:
            p1+=x+1
    return [p1,p2]

def part1(r):
    print("Part1: ", r[0])

def part2(r):
    print("Part2: ", r[1])

result = solve(readInput)
part1(result)
part2(result)