import sys
import itertools
import copy

def readInput():
    return open(sys.argv[1])

def solve(f):
    stars=[]
    r=0
    c=0
    for line in f.readlines():
        for y in range(len(line)):
            c= len(line)
            if line[y] == "#":
                stars.append([r,y])
        r+=1
    rows = [x for x in range(r)]
    columns = [x for x in range(c)]
    for star in stars:
        try:
            rows.remove(star[0])
        except:
            pass
        try:
            columns.remove(star[1])
        except:
            pass
    rowscopy = copy.deepcopy(rows)
    columnscopy = copy.deepcopy(columns)
    starscopy = copy.deepcopy(stars)
    for x in range(len(rowscopy)):
        rowscopy[x] = rowscopy[x] + ((999999*x))
    for y in range(len(columnscopy)):
        columnscopy[y] = columnscopy[y] +((999999*y))
    for x in range(len(rows)):
        rows[x] = rows[x]+x
    for y in range(len(columns)):
        columns[y]=columns[y]+y
    for x in rowscopy:
        for y in range(len(starscopy)):
            if starscopy[y][0] > x:
                starscopy[y][0] = starscopy[y][0]+1000000-1
    for x in columnscopy:
        for y in range(len(starscopy)):
            if starscopy[y][1]>x:
                starscopy[y][1]=starscopy[y][1]+1000000-1
    for x in rows:
        for y in range(len(stars)):
            if stars[y][0]>x:
                stars[y][0]=stars[y][0]+1
    for x in columns:
        for y in range(len(stars)):
            if stars[y][1]>x:
                stars[y][1]=stars[y][1]+1
    allstars = list(itertools.product(stars, stars))
    allstarscopy = list(itertools.product(starscopy,starscopy))
    result1 = 0
    result2=0
    for star in allstarscopy:
        res = (abs(star[0][0]-star[1][0])+abs(star[0][1]-star[1][1]))
        result2+=res
    for star in allstars:
        res = (abs(star[0][0]-star[1][0])+abs(star[0][1]-star[1][1]))
        # print(star, res)
        result1 += res
    return [result1 //2,result2//2]

solution = solve(readInput())
print("Part1: ", solution[0])
print("Part2: ", solution[1])