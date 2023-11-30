lines = []
while True:
    try:
        lines.append(input())
    except EOFError as e:
        break;
for line in lines:
    print(line)