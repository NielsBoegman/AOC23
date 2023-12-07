import sys

cardDict={'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
cardDict2={'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':1,'Q':12,'K':13,'A':14}

def readInput():
    return open(sys.argv[1])

def fullHouse(hand, p2):
    temp = sorted(hand)
    jcount = 0
    for x in hand:
        if x == 1:
            jcount +=1
    print("jcount: ", jcount)
    streak = 1
    start =0
    if p2:
        start = 1
    for x in range(start,4):
        if temp[x] == temp[x+1]:
            streak+=1
        else:
            break
    if p2:
        match jcount:
            case 3:
                return False
            case 2:
                return False
            case 1: 
                if streak ==2:
                    return True
                else:
                    return False
    return streak ==2 or streak == 3

def detectPair(hand, p2):
    jcount = 0
    for x in hand:
        if x == 1:
            jcount +=1
    if p2:
        if jcount == 1:
            return False
        else:
            return True
    temp = sorted(hand)
    finalstreak = 1
    streak = 1
    for x in range(0,4):
        if temp[x] == temp[x+1]:
            streak += 1
        else:
            finalstreak = max(streak, finalstreak)
            streak = 1
    return finalstreak == 2

def handScore(hand):
    return 100000000*hand[0] + 1000000*hand[1]+10000*hand[2]+100*hand[3]+hand[4]

def calcScore(hand, p2):
    x = len(set(hand))
    if p2:
        if 1 in hand:
            x -=1
    match x:
        case 0: return 70000000000 + handScore(hand)
        case 1: return 70000000000 + handScore(hand)
        case 2:
            if fullHouse(hand, p2):
                return 50000000000 + handScore(hand)
            else:
                return 60000000000 + handScore(hand)
        case 3:
            if detectPair(hand, p2):
                return 30000000000 + handScore(hand)
            else:
                return 40000000000 + handScore(hand)
        case 4: return 20000000000 + handScore(hand)
        case 5: return 10000000000 + handScore(hand)


def part1(f):
    hands = []
    hands2 = []
    score = 0
    score2 = 0
    for line in f.readlines():
        temp = []
        temp2 = []
        hand,bid = line.split()
        for x in hand:
            temp.append(cardDict[x])
            temp2.append(cardDict2[x])
        hands.append([calcScore(temp, False), temp, int(bid)])
        hands2.append([calcScore(temp2, True), temp2, int(bid)])
    hands2_sorted = sorted(hands2)
    hands_sorted = sorted(hands)
    for x in range(len(hands2_sorted)):
        score2 += hands2_sorted[x][2]*(x+1)
    for x in range(len(hands_sorted)):
        score += hands_sorted[x][2]*(x+1)
        print("The hand is: ", hands2_sorted[x][1]," with score: ", hands2_sorted[x][0])
    return [score,score2]

file = readInput()
result = part1(file)
print("Part1: ", result[0])
print("Part2: ", result[1])
