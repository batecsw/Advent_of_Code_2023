f = open('input2.txt')
lines = f.readlines()
total = 0
limits = {'red': 12 , 'green': 13 , 'blue': 14}
for line in lines:
    valid = True
    game, restline = line.split(':')
    for handful in restline.split(';'):
        for balls in handful.split(','):
            num, colour = balls.split()
            if int(num) > limits.get(colour):
                valid = False
    if valid:
        total += int(game[5:])
print(total)

