import csv
import random
import sys

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
        return self.list1, self.list2

    def __str__(self):
        return '\n'.join(map(str, self.cards))


class Player:
    def __init__(self):
        self.players_deck = []
        self.has_lost = False

class Game:
    def __init__(self, deck):
        self.player1 = Player()
        self.player2 = Player()
        self.player1.players_deck, self.player2.players_deck = deck.deck_split()
    
    def game_move(self):
        card1 = int(self.player1.players_deck[0].rank)
        card2 = int(self.player2.players_deck[0].rank)
        if card1 > card2:
            return "play1"
        elif card1 < card2:
            return "play2"
        elif card1 == card2:
            return "war"

    
    def __str__(self):
        return f"{self.player1.deck}"

def main():
    deck = Deck('cards.csv')
    #print(deck)
    game = Game(deck)
    while not game.player1.has_lost or not game.player2.has_lost:
        if game.game_move() == "play1":
            game.player1.players_deck.append(game.player2.players_deck[0])
            game.player2.players_deck.pop(0)
            for each in game.player1.players_deck:
                print(each.card)
        print(len(game.player1.players_deck))
        print(len(game.player2.players_deck))
        if len(game.player2.players_deck) == 0:
            print("The second player has lost!")
            game.player2.has_lost = True
            sys.exit()
        if game.game_move() == "play2":
            game.player2.players_deck.append(game.player1.players_deck[0])
            game.player1.players_deck.pop(0)
            for each in game.player2.players_deck:
                print(each.card)
        print("second")
        print(len(game.player1.players_deck))
        print(len(game.player2.players_deck))
        if len(game.player1.players_deck) == 0:
            print("The first player has lost!")
            game.player1.has_lost = True
            sys.exit()

        if game.game_move() == "war":
                war_deck = []
                war_deck.append(game.player1.players_deck[0])
                war_deck.append(game.player2.players_deck[0])
                i = 1
                while game.player1.players_deck[i].rank == game.player2.players_deck[i].rank:
                    war_deck.append(game.player1.players_deck[i])
                    war_deck.append(game.player2.players_deck[i])
                    war_deck.append(game.player1.players_deck[i+1])
                    war_deck.append(game.player2.players_deck[i+1])
                    i += 2
                if game.player1.players_deck[i].rank > game.player2.players_deck[i].rank:
                    game.player1.players_deck.extend(war_deck)
                    del game.player2.players_deck[:i]
                if len(game.player2.players_deck) == 0:
                    print("The second player has lost!")
                    game.player2.has_lost = True
                    sys.exit()
                if game.player1.players_deck[i].rank < game.player2.players_deck[i].rank:
                    game.player2.players_deck.extend(war_deck)
                    del game.player1.players_deck[:i]
                if len(game.player1.players_deck) == 0:
                    print("The first player has lost!")
                    game.player1.has_lost = True
                    sys.exit()
                for each in war_deck:
                    print(each.card)


if __name__ == "__main__":
    main()