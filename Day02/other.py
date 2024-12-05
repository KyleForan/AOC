
data = open('input').read().split("\n")
data = [ 
    [ 
        int(num) for num in line.split(" ") 
    ] for line in data 
    if line
]

differences = [ [ line[i] - line[i-1] for i in range(1, len(line)) ] for line in data ]
safe = 0

for diff in differences:
    if all([x > 0 for x in diff]) or all([x < 0 for x in diff]):
        if max([ abs(x) for x in diff]) <= 3:
            safe += 1

# print(data, differences)
print(safe)