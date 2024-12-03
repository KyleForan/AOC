import numpy as np

data = open('input').read().split("\n")
data = [ 
    [ 
        int(num) for num in line.split(" ") 
    ] for line in data 
    if line
]

differences = map(lambda arr: np.diff(np.array(arr)), data)
safe = 0

for diff in differences:
    if all([x > 0 for x in diff]) or all([x < 0 for x in diff]):
        if max([ abs(x) for x in diff]) <= 3:
            safe += 1

print(safe)