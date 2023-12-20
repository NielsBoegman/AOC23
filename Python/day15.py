import sys

def readInput():
    return open(sys.argv[1])

def hash(key):
    cv = 0
    for x in key:
        cv += ord(x)
        cv *= 17
        cv = cv%256
    return cv

def solve(f):
    res1 = 0
    boxes = [[] for i in range(256)]
    for x in f.readline().split(","):
        res1 += hash(x)
        temp = []
        minus = False
        if "-" in x:
            temp = x.split("-")
            minus = True
        if "=" in x:
            temp = x.split("=")
        box = hash(temp[0])
        if minus:
            for z in range(len(boxes[box])):
                if boxes[box][z][0] == temp[0]:
                    del boxes[box][z]
                    break
        else:
            same = True
            for z in range(len(boxes[box])):
                if boxes[box][z][0] == temp[0]:
                    boxes[box][z][1] = int(temp[1])
                    same = False
            if same:
                boxes[box].append([temp[0],int(temp[1])])
    res2 = 0
    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            value = (x+1)*(y+1)*boxes[x][y][1]
            res2 += value
    return [res1,res2]

result = solve(readInput())
print("Part1: ", result[0])
print("Part2: ", result[1])
