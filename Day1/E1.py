
data = open("input").read().split("\n")

rhs = []
lhs = []

for line in data:
    x, y = line.split("   ")
    lhs.append(x)
    rhs.append(y)

rhs.sort()
lhs.sort()

diff = []
for i in range(len(rhs)):
    difference = int(rhs[i]) - int(lhs[i])
    diff.append(abs(difference))


print(sum(diff))
