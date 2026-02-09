import re

pattern = re.compile('[A-Z]+')
test = "HELLO"

testmatch = pattern.match(test)

print(testmatch.group() == test)
