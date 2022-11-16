import re

with open("./regex_test.txt")as f:
    data = f.readlines()

for person in data:
    pattern = re.match(r'[A-Za-z]+[" "][A-Z][ A-Za-z]+', person)
    if pattern:
        print(pattern.group())
    else:
        print(None)