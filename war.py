import csv
import random
import sys

class Card:
    """
    Represents a playing card.

    Attributes:
        unicode (str): Unicode symbol of the card.
        card (str): Name of the card.
        rank (str): Rank of the card.
    """
    def __init__(self, unicode, card, rank):
        self.unicode = unicode
        self.card = card
        self.rank = rank
    
    def __str__(self):
        return f"{self.unicode} {self.card} ({self.rank})"
    
class Deck:
    """
    Represents a deck of cards.

    Attributes:
        file_csv (str): CSV file containing card information.
        cards (list): List of Card objects representing the deck.
        list1 (list): First players deck.
        list2 (list): Second players deck.
    """
    def __init__(self, file_csv):
        self.cards = []
        self.load_cards(file_csv)
        self.shuffle_deck()
    
    def load_cards(self, file_csv):
        """
        Loads cards from a CSV file into the deck.
        """
        with open(file_csv, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.cards.append(Card(row['Unicode'], row['Card'], row['Rank']))
    
    def shuffle_deck(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)
    
    def deck_split(self):
        """
        Splits the deck into two halves.

        Returns:
            tuple: Two lists representing each split of the deck.
        """
        num_of_cards_for_each = len(self.cards) // 2
        self.list1 = self.cards[:num_of_cards_for_each]
        self.list2 = self.cards[num_of_cards_for_each:]
        return self.list1, self.list2

    def __str__(self):
        return '\n'.join(map(str, self.cards))


class Player:
    """
    Represents a player in the card game.

    Attributes:
        players_deck (list): List of Card objects representing the player's deck.
        has_lost (bool): Indicates if the player has lost the game.
    """
    def __init__(self):
        self.players_deck = []
        self.has_lost = False

class Game:
    """
    Represents the card game.

    Attributes:
        player1 (Player): First player.
        player2 (Player): Second player.
    """
    def __init__(self, deck):
        self.player1 = Player()
        self.player2 = Player()
        self.player1.players_deck, self.player2.players_deck = deck.deck_split()
    
    def game_move(self):
        """
        Determines the outcome of a move in the game.

        Returns:
            str: Outcome of the move - 'play1', 'play2', or 'war'.
        """
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
    game = Game(deck)
    while (not game.player1.has_lost or not game.player2.has_lost) and input("Enter y to play:") == "y":
        match game.game_move():
            case "play1":
                print(f"{game.player1.players_deck[0].rank} vs {game.player2.players_deck[0].rank}")
                print(f"{game.player1.players_deck[0].card} vs {game.player2.players_deck[0].card}")
                
                game.player1.players_deck.append(game.player1.players_deck[0])
                game.player1.players_deck.pop(0)
                game.player1.players_deck.append(game.player2.players_deck[0])
                game.player2.players_deck.pop(0)

                print(f"{len(game.player1.players_deck)}  {len(game.player2.players_deck)}")

                if len(game.player2.players_deck) == 0:
                    print("The second player has lost!")
                    game.player2.has_lost = True
                    sys.exit()
                pass

            case "play2":
                print(f"{game.player1.players_deck[0].rank} vs {game.player2.players_deck[0].rank}")
                print(f"{game.player1.players_deck[0].card} vs {game.player2.players_deck[0].card}")
                
                game.player2.players_deck.append(game.player2.players_deck[0])
                game.player2.players_deck.pop(0)
                game.player2.players_deck.append(game.player1.players_deck[0])
                game.player1.players_deck.pop(0)

                print(f"{len(game.player1.players_deck)}  {len(game.player2.players_deck)}")
        
                if len(game.player1.players_deck) == 0:
                    print("The first player has lost!")
                    game.player1.has_lost = True
                    sys.exit()
                
                pass
        
            case "war":
                war_deck = []
                
                print("war")
                print(f"{game.player1.players_deck[0].rank} vs {game.player2.players_deck[0].rank}")
                print(f"{game.player1.players_deck[0].card} vs {game.player2.players_deck[0].card}")
                print(f"{game.player1.players_deck[1].unicode} vs {game.player2.players_deck[1].unicode}")

                war_deck.append(game.player1.players_deck[0])
                game.player1.players_deck.pop(0)
                war_deck.append(game.player2.players_deck[0])
                game.player2.players_deck.pop(0)
                
                
                i = 2
                while int(game.player1.players_deck[i].rank) == int(game.player2.players_deck[i].rank):
                    print(f"{game.player1.players_deck[i].rank} vs {game.player2.players_deck[i].rank}")
                    print(f"{game.player1.players_deck[i].card} vs {game.player2.players_deck[i].card}")
                    print(f"{game.player1.players_deck[i-1].unicode} vs {game.player2.players_deck[i-1].unicode}")


                    war_deck.append(game.player1.players_deck[i-1])
                    game.player1.players_deck.pop(i-1)
                    war_deck.append(game.player2.players_deck[i-1])
                    game.player2.players_deck.pop(i-1)
                    war_deck.append(game.player1.players_deck[i])
                    game.player1.players_deck.pop(i)
                    war_deck.append(game.player2.players_deck[i])
                    game.player2.players_deck.pop(i)
                    
                    i += 2

                if int(game.player1.players_deck[i].rank) > int(game.player2.players_deck[i].rank):
                    print(f"{game.player1.players_deck[i].rank} vs {game.player2.players_deck[i].rank}")
                    print(f"{game.player1.players_deck[i].card} vs {game.player2.players_deck[i].card}")
                    
                    war_deck.append(game.player1.players_deck[i-1])
                    game.player1.players_deck.pop(i-1)
                    war_deck.append(game.player2.players_deck[i-1])
                    game.player2.players_deck.pop(i-1)
                    war_deck.append(game.player1.players_deck[i])
                    game.player1.players_deck.pop(i)
                    war_deck.append(game.player2.players_deck[i])
                    game.player2.players_deck.pop(i)
                    game.player1.players_deck.extend(war_deck)
                    
                    print(f"{len(game.player1.players_deck)}  {len(game.player2.players_deck)}")

                    if len(game.player2.players_deck) == 0:
                        print("The second player has lost!")
                        game.player2.has_lost = True
                        sys.exit()
                    pass
                
                elif int(game.player1.players_deck[i].rank) < int(game.player2.players_deck[i].rank):
                    print(f"{game.player1.players_deck[i].rank} vs {game.player2.players_deck[i].rank}")
                    print(f"{game.player1.players_deck[i].card} vs {game.player2.players_deck[i].card}")
                    
                    war_deck.append(game.player1.players_deck[i-1])
                    game.player1.players_deck.pop(i-1)
                    war_deck.append(game.player2.players_deck[i-1])
                    game.player2.players_deck.pop(i-1)
                    war_deck.append(game.player1.players_deck[i])
                    game.player1.players_deck.pop(i)
                    war_deck.append(game.player2.players_deck[i])
                    game.player2.players_deck.pop(i)
                    game.player2.players_deck.extend(war_deck)
                    
                    print(f"{len(game.player1.players_deck)}  {len(game.player2.players_deck)}")

                if len(game.player1.players_deck) == 0:
                    print("The first player has lost!")
                    game.player1.has_lost = True
                    sys.exit()
                

if __name__ == "__main__":
    main()