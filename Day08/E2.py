from collections import defaultdict
from itertools import combinations

data = open('Day08/input').read().replace('#', '.')
grid = [ list(line) for line in data.split("\n")]
gridHeight, gridWidth = len(grid), len(grid[0])

antennas = defaultdict(list)

inBounds = lambda coords: coords[0] >= 0 and coords[0] < gridHeight and coords[1] >= 0 and coords[1] < gridWidth 
addCords = lambda c1, c2: (c1[0]+c2[0], c1[1]+c2[1])

for x in range(gridHeight):
    for y in range(gridWidth):
        if grid[x][y] != '.':
            antennas[grid[x][y]].append((x, y))

for frequency in antennas:
    for p1, p2 in combinations(antennas[frequency],2):

        posChange = [p1[0]-p2[0], p1[1]-p2[1]]
        negChange = [p2[0]-p1[0], p2[1]-p1[1]]
        
        curr = p1
        while True:
            temp = addCords(curr, posChange)
            if not inBounds(temp):
                break
            
            curr = temp
            if grid[curr[0]][curr[1]] == '.': grid[curr[0]][curr[1]] = '#'

        curr = p2
        while True:
            temp = addCords(curr, negChange)
            if not inBounds(temp):
                break
            
            curr = temp
            if grid[curr[0]][curr[1]] == '.': grid[curr[0]][curr[1]] = '#'
        
print(
    (len(grid) * len(grid[0])) - sum([line.count('.') for line in grid]) 
)
