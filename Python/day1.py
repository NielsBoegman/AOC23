import re
inp = []
replacement = {"one": "on1e", "two": "tw2o", "three":"th3ree", "four":"fo4ur","five":"fi5ve","six":"si6x","seven":"se7ven","eight":"eig8ht","nine":"ni9ne"}

def readInput():
    while True:
        try:
            inp.append(input())
        except EOFError as e:
            break;

def calcSum(inp):
    sum = 0
    for line in inp:
        li = re.sub("\D", '', line)
        sum += int((li[0]) + li[-1])
    return sum

def part1():
    print("Part1: ", calcSum(inp))

def part2():
    for x in range(len(inp)):
        for key in replacement.keys():
           inp[x] = re.sub(key, replacement[key], inp[x]) 
    print("Part2: ", calcSum(inp))

readInput()
part1()
part2()