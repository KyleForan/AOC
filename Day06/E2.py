data = open("Day06/input").read()
grid = [ list(line) for line in data.split("\n") ]

directions =  [[-1, 0], [0, 1], [1, 0], [0, -1]]
currentDirection = 0

# Find 
x = y = 0
for i, line in enumerate(grid):
    if '^' in line:
        sh, sd = [i, line.index("^") ]
        break

x, y = [sh, sd]
grid[x][y] = '.'

path = set()

while True:
    next_pos = x + directions[currentDirection][0], y + directions[currentDirection][1]
    j, k = next_pos
    path.add((x, y))
    # grid[x][y] = 'x'

    if 0 > j or j >= len(grid) or 0 > k or k >= len(grid[0]):
        break

    if grid[j][k] == '#':
        currentDirection += 1
        currentDirection %= 4

        continue
    
    x, y = next_pos


def part1Again(startI, startJ, matrix):
    new_direction = 0

    newPath = set([(startI, startJ, new_direction)])

    while True:
        nextI, nextJ = [(-1, 0), (0, 1), (1, 0), (0, -1)][new_direction]
        nextI, nextJ = startI + nextI, startJ + nextJ

        if not (0 <= nextI < len(matrix) and 0 <= nextJ < len(matrix[0])):
            break

        if matrix[nextI][nextJ] == '#':
            new_direction = (new_direction + 1) % 4
            continue

        startI, startJ = nextI, nextJ

        if (startI, startJ, new_direction) in newPath:
            return 1
        else:
            newPath.add((startI, startJ, new_direction))

    return 0


result = 0

for i, j in path:
    grid[i][j] = '#'
    result += part1Again(sh, sd, grid)
    grid[i][j] = '.'

print(result)
