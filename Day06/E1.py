from pprint import pprint

data = open("Day06/input").read()
grid = [ list(line) for line in data.split("\n") ]

directions =  [[-1, 0], [0, 1], [1, 0], [0, -1]]
currentDirection = 0

# Find 
x = y = 0
for i, line in enumerate(grid):
    if '^' in line:
        x, y = [i, line.index("^") ]
        break


while True:
    next_pos = x + directions[currentDirection][0], y + directions[currentDirection][1]
    j, k = next_pos

    if 0 > j or j >= len(grid) or 0 > k or k >= len(grid[0]):
        break

    if grid[j][k] == '#':
        currentDirection += 1
        currentDirection %= 4

        continue
    
    grid[x][y] = 'x'
    x, y = next_pos

result = [ line.count('x') for line in grid]
print(sum(result)+1)

# pprint(grid)