import sys

def readInput():
    return open(sys.argv[1])

direction = {"R":[0,1],"L":[0,-1],"D":[1,0],"U":[-1,0]}
trans = {0:"R",1:"D",2:"L",3:"U"}

def treatLine(letter, dist, start):
    delta = [direction[letter][0]*int(dist),direction[letter][1]*int(dist)]
    startnew = [start[0]+delta[0],start[1]+delta[1]]
    return startnew

def shoelace(vertices, surrounding, corners):
    x,y = 0,0
    for i in range(len(vertices)):
        x+=(vertices[i][0]*vertices[(i+1)%len(vertices)][1])
        y+=(vertices[i][1]*vertices[(i+1)%len(vertices)][0])
    return ((abs(x-y))/2) +((surrounding-corners)/2) + (((corners-4)/2)/4) + ((corners/2+2)*0.75)

def solve(f):
    vertices1,vertices2 = [],[]
    surrounding1,surrounding2 = 0,0
    corners = 0
    start1, start2 = [0,0],[0,0]
    for line in f.readlines():
        corners +=1
        l = line.split()
        l[2] = ''.join(list(filter(lambda ch: ch not in "()#", l[2])))
        letter = trans[int(l[2][-1])]
        dist = int(l[2][:5], 16)
        surrounding2+=dist
        start2 = treatLine(letter, dist, start2)
        surrounding1 += int(l[1])
        start1 = treatLine(l[0],l[1],start1)
        vertices1.append(start1)
        vertices2.append(start2)
    vertices1.reverse()
    vertices2.reverse()
    result1 = shoelace(vertices1, surrounding1, corners)
    result2 = shoelace(vertices2, surrounding2, corners)
    return [result1, result2]

solution = solve(readInput())
print("Part1: ", solution[0])
print("Part2: ", solution[1])