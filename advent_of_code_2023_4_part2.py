f = open('input4.txt')
lines = f.readlines()
total = 0
cards = []
for line in lines:
    cards.append(1)
i = 0
l = len(cards)

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
                score += 1
    for sc in range(score):
        card_ind = i + sc + 1
        if(card_ind <= l):
            cards[card_ind] += cards[i]
    print(i, cards[i])
    i += 1

for card in cards:
        total += card
print(total)

