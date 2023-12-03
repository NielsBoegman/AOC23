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

def findNumber(x,start,end, inp):
    num = ""
    for i in range(start, end+1):
        num+=inp[x][i]
    return int(num)    

def findNumberHard(x,y,inp):
    start = 0
    end = len(inp[x])-1
    for i in range(y,-1,-1):
        if not inp[x][i].isdigit():
            start = i+1
            break
    for i in range(start, len(inp[x])):
        if not inp[x][i].isdigit():
            end = i-1
            break
    return [findNumber(x, start, end, inp), end]

def checkNumber(x,y, inp):
    directions = {1:[-1,-1], 2:[-1,0], 3:[-1,1], 4:[0,-1], 5:[0,1], 6:[1,-1], 7:[1,0], 8:[1,1]}
    for dir in directions.values():
        nx = x+dir[0]
        ny = y+dir[1]
        lastline = x == len(inp)-1
        if not (nx<0 or nx>=len(inp) or ny<0 or ny>=len(inp[x])-1+lastline):
            if (not inp[nx][ny].isdigit()) and (not inp[nx][ny] == '.'):
                return True
    return False

def checkStar(x,y,inp):
    ratio = []
    for i in range(-1,2):
        if not (x+i<0 or x+i>=len(inp)):
            end = 0
            for j in range(-1,2):
                if not (y+j<0 or y+j>len(inp[x])-1):
                    if not end >= y+j:
                        if inp[x+i][y+j].isdigit():
                            temp = findNumberHard(x+i, y+j, inp)
                            ratio.append(temp[0])
                            end = temp[1]
                            if temp[1] > y:
                                break
    return ratio

def solve(inp):
    part1 = 0
    part2 = 0
    for x in range (len(inp)):
        start = 0
        digit = False
        valid = False
        for y in range(len(inp[x])):
            if inp[x][y].isdigit():
                if not digit:
                    digit = True
                    start = y
                    valid = checkNumber(x,y, inp)
                else:
                    valid = valid or checkNumber(x,y, inp)
            elif digit:
                digit = False
                if valid:
                    part1+=findNumber(x, start, y-1, inp)
                valid = False
                start = 0
            if inp[x][y] == '*':
                ratios = checkStar(x,y,inp)
                if len(ratios) == 2:
                    part2+=ratios[0]*ratios[1]
    return [part1, part2]

solution = solve(readInput().readlines())
print("Part1: ", solution[0])
print("Part2: ", solution[1])