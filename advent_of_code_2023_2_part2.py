# Write your code here :-)
f = open('input2.txt')
lines = f.readlines()
total = 0
for line in lines:
    max_balls = {'red': 0 , 'green': 0 , 'blue': 0}
    game, restline = line.split(':')
    for handful in restline.split(';'):
        for balls in handful.split(','):
            num, colour = balls.split()
            if int(num) > max_balls.get(colour):
                max_balls.update({colour : int(num)})
    product = max_balls.get("red")*max_balls.get("blue")*max_balls.get("green")
    print(max_balls, product)
    total += product
print(total)
