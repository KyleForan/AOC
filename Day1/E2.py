from collections import Counter
data = open("input").read().split("\n")

rhs = []
lhs = []

for line in data:
    x, y = line.split("   ")
    lhs.append(int(x))
    rhs.append(int(y))

hashmap = Counter(rhs)

totalArr = []
for i in lhs:
    x = hashmap[i]
    totalArr.append(i*x)

print(sum(totalArr))