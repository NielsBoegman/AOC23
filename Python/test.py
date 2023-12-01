import re
test="one23one"
test = re.sub('one', '1', test)
# print(int(test[0]+test[-1]))
print(test)