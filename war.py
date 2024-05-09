import csv
import random

class Card:
    def __init__(self, unicode, card, rank):
        self.unicode = unicode
        self.card = card
        self.rank = rank
    
    def __str__(self):
        return f"{self.unicode} {self.card} ({self.rank})"
    
class Deck:
    def __init__(self, file_csv):
        self.cards = []
        self.load_cards(file_csv)
        self.shuffle_deck()
    
    def load_cards(self, file_csv):
        with open(file_csv, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.cards.append(Card(row['Unicode'], row['Card'], row['Rank']))
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def deck_split(self):
        num_of_cards_for_each = len(self.cards) // 2
        self.list1 = self.cards[:num_of_cards_for_each]
        self.list2 = self.cards[num_of_cards_for_each:]

    def __str__(self):
        return '\n'.join(map(str, self.cards))


class Player:
    ...

class Game:
    ...

def main():
    deck = Deck('cards.csv')
    print(deck)


if __name__ == "__main__":
    main()