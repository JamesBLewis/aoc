input = []
with open('input.txt') as f:
    for line in f:
        values = line.split(':')[1].strip('\n').split(';')
        for i in range(len(values)):
            values[i] = values[i].strip(' ').split(', ')
        input.append(values)
print(input)

output = 0

for game in input:
    game_max = {'red': 0, 'green': 0, 'blue': 0}
    for hand in game:
        for cube in hand:
            values = cube.split(' ')
            game_max[values[1]] = max(game_max[values[1]], int(values[0]))
    output += game_max['red'] * game_max['green'] * game_max['blue']
print(output)