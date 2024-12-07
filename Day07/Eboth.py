data = open('Day07/input').read().split('\n')
total = 0

for line in data:
    if not line: continue
    result, nums = line.split(': ')

    result = int(result)
    nums = [int(num) for num in nums.split(' ')]

    possibilities = [nums.pop(0)]

    for num in nums:
        tempPossibilities = []
        for p in possibilities:
            # Part 2 is this line ↓
            # tempPossibilities.append(int(str(p) + str(num))) 
            tempPossibilities.append(p + num)
            tempPossibilities.append(p * num)
        possibilities = tempPossibilities

    if result in possibilities: total += result

print(total)