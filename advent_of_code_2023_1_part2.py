# Write your code here :-)
f = open('input2.txt')
lines = f.readlines()
total = 0
for line in lines:
    valid = True
    game, restline = line.split(':')
    print game, restline
print(total)
