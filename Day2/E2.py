import numpy as np

data = open('input').read().split("\n")
data = [ 
    [ 
        int(num) for num in line.split(" ") 
    ] for line in data 
    if line
]

def check(line) -> int:
    diff = np.diff(np.array(line))
    
    if all([x > 0 for x in diff]) or all([x < 0 for x in diff]):
        if max([ abs(x) for x in diff]) <= 3:
            return 1

    return 0

safe = 0

for line in data: 
    for i in range(len(line)):
        sub = line[:i] + line[i+1:]
        
        if check(sub):
            safe += 1
            break

print(safe)