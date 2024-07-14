import random
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

class UnoCard:
    def __init__(self, color, value):
        self.color = color
        self.value = value

class UnoGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [[] for _ in range(num_players)]
        self.deck = self.create_deck()
        self.discard_pile = []
        
    def create_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = list(range(10)) + ['Skip', 'Reverse', 'Draw Two']
        deck = [UnoCard(color, value) for color in colors for value in values]
        return deck * 2  # Zwei von jeder Karte
    
    def deal_cards(self):
        random.shuffle(self.deck)
        for _ in range(7):
            for player in self.players:
                player.append(self.deck.pop())
        self.discard_pile.append(self.deck.pop())
    
    def reshuffle_discard_pile(self):
        if not self.deck:
            top_card = self.discard_pile.pop()
            self.deck = self.discard_pile
            random.shuffle(self.deck)
            self.discard_pile = [top_card]
    
    def play_game(self):
        self.deal_cards()
        current_player = 0
        while all(len(player) > 0 for player in self.players):
            self.reshuffle_discard_pile()  # Überprüfen und ggf. neu mischen
            top_card = self.discard_pile[-1]
            playable_cards = [card for card in self.players[current_player] 
                              if card.color == top_card.color or card.value == top_card.value]
            if playable_cards:
                played_card = random.choice(playable_cards)
                self.players[current_player].remove(played_card)
                self.discard_pile.append(played_card)
            else:
                if self.deck:
                    self.players[current_player].append(self.deck.pop())
                else:
                    # Wenn das Deck leer ist und keine Karte gespielt werden kann, den nächsten Spieler an die Reihe lassen
                    pass
            current_player = (current_player + 1) % self.num_players
        return self.players.index(next(player for player in self.players if len(player) == 0))
        
def simulate_games(num_games, num_players):
    results = []
    for _ in range(num_games):
        game = UnoGame(num_players)
        winner = game.play_game()
        results.append(winner)
    return results

# Simulation and analysis
num_games = 10000
num_players = 4
results = simulate_games(num_games, num_players)

# Data analysis
df = pd.DataFrame({'winner': results})
win_counts = df['winner'].value_counts()

# Visualization
plt.figure(figsize=(10, 6))
win_counts.plot(kind='bar')
plt.title('Uno Game Winner Distribution')
plt.xlabel('Player')
plt.ylabel('Number of Wins')
plt.show()

# Print statistics
print(win_counts)
print(f"\nWin percentages:\n{win_counts / num_games * 100}")