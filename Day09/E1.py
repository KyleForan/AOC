data = open('Day09/input').read()

# ans = "0099811188827773336446555566.............."
# ans = '022111222......'

# modes = ['id', 'free']
mode = 0

# print(data)
amphipod = ''
currId = 0

amphipod = list(amphipod)

for el in data:
    el = int(el)

    if mode == 1:
        for _ in range(el):
            amphipod.append('.')
    else:
        for _ in range(el):
            amphipod.append(str(currId))
        
        currId += 1

    mode = (mode + 1) % 2

print("Got Amphipods.")
# print(amphipod)

numIndexes = [i for i, el in enumerate(amphipod) if el != '.']

print("Got NumIndexes")


for i in range(len(amphipod)):
    # if all([el == '.' for el in amphipod[i:]]): break
    if numIndexes[-1] <= i: break
    if amphipod[i] == '.':
        lastIndex = numIndexes.pop()
        amphipod[i] = amphipod[lastIndex]
        amphipod[lastIndex] = '.'
        ...

print("Compressed Amphipods.")

# amphipod = ''.join(amphipod)

checksum = sum([
    int(x) * i for i, x in enumerate(amphipod) if x != '.'
])

print(checksum)
from pprint import pprint
# print(amphipod)
# print(''.join(amphipod) == ans)

