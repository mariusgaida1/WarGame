import csv
import random

class Card:
    def __init__(self, unicode, card, rank):
        self.unicode = unicode
        self.card = card
        self.rank = rank
    
    def __str__(self):
        return f"{self.unicode} {self.card} ({self.rank})"
    
    def __repr__(self):
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
        player1_deck = self.cards[:num_of_cards_for_each]
        player2_deck = self.cards[num_of_cards_for_each:]
        return player1_deck, player2_deck

    def __str__(self):
        return '\n'.join(map(str, self.cards))

class Player:
    def __init__(self):
        self.players_deck = []
        self.has_lost = False

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
    
    def assign_cards(self, deck):
        deck1, deck2 = deck.deck_split()
        self.player1.players_deck = deck1
        self.player2.players_deck = deck2

    def fight(self):
        while not self.player1.has_lost and not self.player2.has_lost:
            if self.player1.players_deck[0][2] == self.player2.players_deck[0][2]:
                self.war()

    def war(self):
        pass
    
def main():
    deck = Deck('cards.csv')
    game = Game()
    game.assign_cards(deck)
    start = input("Would you like to start the game? ")
    if start or start == "":
        game.fight()

if __name__ == "__main__":
    main()