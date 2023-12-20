import sys
import re

def readInput():
    return open(sys.argv[1])

def solve(f):
    works = {}
    res1=0
    i = False
    for line in f.readlines():
        if line == "\n":
            i = True
            continue
        if not i:
            name,order= line.split("{")
            order = order.replace('}','')
            order = order.strip()
            orders = order.split(",")
            for o in range(len(orders)-1):
                orders[o] = orders[o].split(":")
            orders[-1] = ["True", orders[-1]]
            works[name]=orders
        else:
            x,m,a,s = map(int, re.findall(r'\d+', line))
            next = "in"
            while not (next == "R" or next == "A"):
                steps = works[next]
                for step in steps:
                    if eval(step[0]):
                        next = step[1]
                        break
            if next == 'A':
                res1+= (x+m+a+s)
                continue
    return res1

print("Part1: ",solve(readInput()))                  
                