import re
test = "Game 1: bla, bla, bla"
test = re.sub("Game \d: ", "", test) 
print(test)