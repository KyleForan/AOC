data = open('Day07/input').read().split('\n')
total = [0, 0]

for line in data:
    if not line: continue
    result, nums = line.split(': ')

    result = int(result)
    nums = [int(num) for num in nums.split(' ')]

    possibilities = [(nums.pop(0), 1)]

    for num in nums:
        tempPossibilities = []
        for possible, part in possibilities:
            tempPossibilities.append((int(str(possible) + str(num)), 2)) 
            tempPossibilities.append((possible + num, part))
            tempPossibilities.append((possible * num, part))
        possibilities = tempPossibilities

    part1 = result in [el[0] for el in possibilities if el[1] == 1]
    part2 = result in [el[0] for el in possibilities]
    
    total = [total[0] + (result * part1), total[1] + (result * part2)]

print(f"Part1: {total[0]}")
print(f"Part2: {total[1]}")