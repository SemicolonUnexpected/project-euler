from collections import Counter

path = "/storage/emulated/0/Documents/Project Euler/0054_poker.txt"
file = open(path)
text = file.read()[:-1]
lines = text.split("\n")
hands = [line.split() for line in lines]

cards = "23456789TJQKA"

card_values = {cards[i]: i + 2 for i in range(13)}

straights = [tuple([i + 5, i + 4, i + 3, i + 2, i + 1]) for i in range(1, 10)]
straights.append(tuple([14, 5, 4, 3, 2]))
straights = set(straights)

ranks = {
    (1, 1, 1, 1, 1): 1,
    (2, 1, 1, 1): 2,
    (2, 2, 1): 3,
    (3, 1, 1): 4,
    (3, 2): 7,
    (4, 1): 8,
}


def sort_hand(hand):
    counter = Counter([card[0] for card in hand])
    values = [(counter[i], card_values[i]) for i in counter]
    values = sorted(values, reverse=True)
    duplicates, values = zip(*values)
    return duplicates, values


def score_hand(hand):
    suits = set([card[1] for card in hand])
    is_flush = len(suits) == 1
    hand = sort_hand(hand)
    is_straight = hand[1] in straights
    score = 0
    if is_straight and is_flush:
        score = 9
    elif is_straight:
        score = 5
    elif is_flush:
        score = 6
    else:
        score = ranks[hand[0]]
    return score, hand[1]


wins = 0
for hand in hands:
    one = score_hand(hand[:5])
    two = score_hand(hand[5:])
    if one[0] > two[0]:
        wins += 1
        continue
    if two[0] > one[0]:
        continue
    for i, j in zip(one[1], two[1]):
        if i > j:
            wins += 1
            break
        if j > i:
            break

print(wins)

