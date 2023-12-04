import sys

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

def part2(matches):
    for i in range(len(matches)):
        for j in range(1,matches[i][1]+1):
            matches [i+j][0]+=matches[i][0]
    score = 0
    for match in matches:
        score+=match[0]
    return score

def solve(f):
    part1 = 0
    matches = []
    for line in f.readlines():
        s=[]
        l = line.split(":")
        l = l[1].split("|")
        for x in range(2):
            l[x]=l[x].split()
            map(int, l[x])
            s.append(set(l[x]))
        s2 = len(s[0].intersection(s[1]))
        matches.append([1,s2])
        if s2>0:
            part1+=2**(s2-1)
    print("Part1: ", part1)
    print("Part2: ", part2(matches))

solve(readInput())