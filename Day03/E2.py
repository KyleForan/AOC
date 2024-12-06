import re

data = open("Day03/input").read()
instructions = re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", data)

total = 0
enable = True

for x, y, inst in instructions:

    if inst:
        enable = "n't" not in inst
    else: 
        total += (int(x) * int(y)) * int(enable)

print(total)