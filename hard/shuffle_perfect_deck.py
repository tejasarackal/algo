import random


def shuffle_iteratively(cards: list):
    for index, card in enumerate(cards):
        choice = random.randint(0, index)
        cards[index] = cards[choice]
        cards[choice] = card
        print(index, cards)


if __name__ == '__main__':
    shuffle_iteratively([i for i in range(52)])