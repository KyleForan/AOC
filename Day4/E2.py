
data = open("Day4/input").read()
data = [ list(line) for line in data.split("\n")]

result = 0

for i, line in enumerate(data[1:-1]):
    for j, el in enumerate(line[1:-1]):

        if el == 'A':
            one = {data[i+2][j+2], data[i][j]} == {'M', 'S'}
            two = {data[i+2][j], data[i][j+2]} == {'M', 'S'}

            if one and two:
                result += 1

print(result)

