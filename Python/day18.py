import sys

def readInput():
    return open(sys.argv[1])

def fillTrench(trench):
    print("fill")
    for i in range(len(trench)):
        c = False
        streak = [0,False]
        for j in range(len(trench[1])):
            sky = [True,True]
            for x in range(i+1,len(trench)):
                if trench[i+1][j] == "!":
                    sky[0]=False
                    break
            for x in range(i):
                if trench[x][j]=="!":
                    sky[1]=False
                    break
            sky = sky[1] and sky[0]
            if sky:
                continue
            if trench[i][j]=="!":
                streak[0]+=1
                streak[1]=True
            if trench[i][j]=="." and j>0 and trench[i][j-1] == "!" and not c:
                c = True
                trench[i][j]="#"
                streak[0]=0
                streak[1] = False
            if trench[i][j]=="." and j>0 and trench[i][j-1] == "!" and c:
                c=False
            if trench[i][j]=="." and c and not trench[i][j-1] == "!":
                trench[i][j]="#"
    for i in range(len(trench)):
        for j in range(len(trench[1])):
            if trench[i][j]=="!":
                trench[i][j]="#"
    for x in range(len(trench)):
        print(trench[x])
    # for i in range(len(trench)):
    #     first = 100000
    #     last = 0
    #     for j in range(len(trench[1])):
    #         if trench[i][j] == "#":
    #             first = j
    #             break
    #     for j in range(len(trench[1])-1,-1,-1):
    #             if trench[i][j] == "#":
    #                 last = j
    #                 break
    #     for j in range(first, last+1):
    #             trench[i][j]="#"
    return trench

def countTrench(trench):
    count = 0
    for i in range(len(trench)):
        for j in range(len(trench[1])):
            if trench[i][j] == "#":
                count+=1
    return count

direction = {"R":[0,1],"L":[0,-1],"D":[1,0],"U":[-1,0]}

def solve(f):
    trench = [['.']*500 for i in range(500)]
    start = [0,0]
    for line in f.readlines():
        l = line.split()
        delta = [direction[l[0]][0]*int(l[1]),direction[l[0]][1]*int(l[1])]
        startnew = [start[0]+delta[0],start[1]+delta[1]]
        if l[0] == "U" or l[0] == "D":
            for x in range(start[0], startnew[0]+direction[l[0]][0],direction[l[0]][0]):
                trench[x][startnew[1]] = "!"
        elif l[0] == "R" or l[0] == 'L':
            for x in range(start[1],startnew[1]+direction[l[0]][1],direction[l[0]][1]):
                trench[startnew[0]][x] = "!"
        start = startnew
    print("prefill")
    for x in range(len(trench)):
        print(trench[x])
    return countTrench(fillTrench(trench))

print(solve(readInput()))