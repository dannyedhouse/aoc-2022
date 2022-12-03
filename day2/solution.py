score_me  = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
score_opponent = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}

def calc_score(score_dict, strategy) -> str:
    res = score_dict[strategy]
    return res

with open('input.txt') as f:
    lines = f.read().splitlines()
    my_total = 0
    opponent_total = 0

    for line in lines:
        my_total += calc_score(score_me, line)
        opponent_total += calc_score(score_opponent, line)

    print(my_total)
    print(opponent_total)