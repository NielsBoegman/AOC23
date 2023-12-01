import re
inp = []
replacement = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
def readInput():
    while True:
        try:
            inp.append(input())
        except EOFError as e:
            break;

def part1():
    sum = 0
    for line in inp:
        temp = re.sub("\D", '', line)
        temp = int(temp[0] + temp[-1])
        sum += temp
    print("Part1: ", sum)

def part2():
    sum = 0
    for line in inp:
        temp = line
        for i in range(1,10):
            repl = list(replacement[i])
            repl.insert(len(repl)//2, str(i))
            repl = "".join(repl)
            temp = re.sub(replacement[i],repl,temp)
        temp = re.sub("\D",'',temp)
        sum+=int(temp[0]+temp[-1])
    print("Part2: ", sum)

readInput()
part1()
part2()