# Write your code here :-)
f = open('input4.txt')
lines = f.readlines()
total = 0
for line in lines:
    card, restline = line.split(':')
    win_line, your_line = restline.split('|')
    score = 0
    win_nums = []
    for win_num in win_line.split():
        win_nums.append(win_num)
    for your_num in your_line.split():
        for win_num in win_nums:
            if win_num == your_num:
                if score == 0:
                    score = 1
                else:
                    score *=2
    total += score
    print(card, score, total)
print(total)
