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
    return f.readlines()

def solve(f):
    part1 = 0
    matches = [1]*len(f)
    for z in range(len(f)):
        s=[]
        l = f[z].split(":")[1].split("|")
        for x in range(2):
            s.append(set(map(int,l[x].split())))
        s2 = len(s[0].intersection(s[1]))
        for j in range(1,s2+1):
            matches[z+j] += matches[z]
        if s2>0:
            part1+=2**(s2-1)
    print("Part1: ", part1)
    print("Part2: ", sum(matches))

solve(readInput())