from collections import defaultdict
from itertools import combinations

data = open('Day08/input').read().replace('#', '.')
grid = [ list(line) for line in data.split("\n")]
gridHeight, gridWidth = len(grid), len(grid[0])

antennas = defaultdict(list)

for x in range(gridHeight):
    for y in range(gridWidth):
        if grid[x][y] != '.':
            antennas[grid[x][y]].append((x, y))

for frequency in antennas:
    for p1, p2 in combinations(antennas[frequency],2):

        changeX, changeY = [p2[0]-p1[0], p2[1]-p1[1]]
        newPoints = [(p1[0] - changeX, p1[1] - changeY), (p2[0] + changeX, p2[1] + changeY)]

        for p in newPoints:
            if p[0] >= 0 and p[0] < gridHeight and p[1] >= 0 and p[1] < gridWidth:
                grid[p[0]][p[1]] = '#'
        
print(
    sum([line.count('#') for line in grid]),
)
