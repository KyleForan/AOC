import numpy as np

data = open("Day4/input").read()
data = [ list(line) for line in data.split("\n")]
npData = np.array(data)

height, width = len(data), len(data[0])

leftRight = data[:]
UpDown = list(map(list, zip(*data)))
downLeft = [ np.diag(npData, x).tolist() for x in range((height)*-1, width)] 
downRight = [ np.diag(npData[::-1], x).tolist() for x in range((height-4)*-1, width-4)] 

result = 0

for arr in [UpDown, leftRight, downLeft, downRight]:
    for sub in arr:
        result += ''.join(sub).count("XMAS") + ''.join(sub).count("XMAS"[::-1])

print(result)

