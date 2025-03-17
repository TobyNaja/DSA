import json

suit_order = {"S": 0, "H": 1, "D": 2, "C": 3}

rank_order = {"K": 0, "Q": 1, "J": 2, "10": 3, "9": 4, "8": 5, "7": 6, 
              "6": 7, "5": 8, "4": 9, "3": 10, "2": 11, "1": 12, "A": 13}

def scorex(lists):
    listscore = []
    for name, pai in lists:
        scores = 0
        for card in pai:
            rank, suit = card[:-1], card[-1]
            if card == "2C" or card == "QS":
                scores += 50
            elif rank == "A":
                scores += 15
            elif rank in {"Q", "10", "K", "J"}:
                scores += 10
            else:
                scores += 5
        listscore.append((name, scores, pai))
    return listscore

def insertion_sort_players(players):
    for i in range(1, len(players)):
        key = players[i]
        j = i - 1
        while j >= 0 and (key[1] > players[j][1] or (key[1] == players[j][1] and key[0] > players[j][0])):
            players[j + 1] = players[j]
            j -= 1
        players[j + 1] = key
    return players

def insertion_sort_pai(pai):
    for i in range(1, len(pai)):
        key = pai[i]
        print(key[:-1])
        j = i - 1
        while j >= 0 and (
            (suit_order[key[-1]] < suit_order[pai[j][-1]]) or
            (suit_order[key[-1]] == suit_order[pai[j][-1]] and rank_order[key[:-1]] < rank_order[pai[j][:-1]])
        ):
            pai[j + 1] = pai[j]
            j -= 1
        pai[j + 1] = key
    return pai

def main():
    lists = []
    player = int(input())
    num_pai = int(input())
    for _ in range(player):
        x = json.loads(input())
        lists.append(x)

    listx = scorex(lists)
    sorted_players = insertion_sort_players(listx)

    for name, score, pai in sorted_players:
        sorted_pai = insertion_sort_pai(pai)
        # print(f"{name} -> {score} -> {sorted_pai}")

main()
