# 12 red cubes, 13 green cubes, and 14 blue cubes?
want = {'red': 12, 'green': 13, 'blue': 14 }
input = []
with open('input.txt') as f:
    for line in f:
        values = line.split(':')[1].strip('\n').split(';')
        for i in range(len(values)):
            values[i] = values[i].strip(' ').split(', ')
        input.append(values)
print(input)
score = 0
gameID = 1
for game in input:
    impossible = False
    for hand in game:
        for cube in hand:
            values = cube.split(' ')
            if want[values[1]] < int(values[0]):
                impossible = True
    if not impossible:
        score += gameID
    gameID += 1
print(score)