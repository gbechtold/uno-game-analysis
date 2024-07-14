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
        self.turns = 0
        self.cards_played = 0
        
    def create_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = list(range(10)) + ['Skip', 'Reverse', 'Draw Two']
        deck = [UnoCard(color, value) for color in colors for value in values]
        return deck * 2
    
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
            self.reshuffle_discard_pile()
            self.turns += 1
            top_card = self.discard_pile[-1]
            playable_cards = [card for card in self.players[current_player] 
                              if card.color == top_card.color or card.value == top_card.value]
            if playable_cards:
                played_card = random.choice(playable_cards)
                self.players[current_player].remove(played_card)
                self.discard_pile.append(played_card)
                self.cards_played += 1
            else:
                if self.deck:
                    self.players[current_player].append(self.deck.pop())
                else:
                    pass
            current_player = (current_player + 1) % self.num_players
        winner = self.players.index(next(player for player in self.players if len(player) == 0))
        return winner, self.turns, self.cards_played

def simulate_games(num_games, num_players):
    results = []
    total_turns = 0
    total_cards_played = 0
    for game_num in range(num_games):
        game = UnoGame(num_players)
        winner, turns, cards_played = game.play_game()
        results.append(winner)
        total_turns += turns
        total_cards_played += cards_played
        if game_num % 1000 == 0:
            print(f"Simulated {game_num} games...")
    return results, total_turns, total_cards_played

# Simulation und Analyse
num_games = 10000
num_players = 4
print(f"Simuliere {num_games} Uno-Spiele mit {num_players} Spielern...")
results, total_turns, total_cards_played = simulate_games(num_games, num_players)

# Datenanalyse
df = pd.DataFrame({'winner': results})
win_counts = df['winner'].value_counts().sort_index()

# Visualisierung
plt.figure(figsize=(10, 6))
win_counts.plot(kind='bar')
plt.title('Uno-Spiel Gewinner-Verteilung')
plt.xlabel('Spieler')
plt.ylabel('Anzahl der Siege')
plt.savefig('uno_results.png')
plt.close()

# Textbasierte Ausgabe
print("\n--- Detaillierte Spielstatistiken ---")
print(f"Gesamtanzahl der simulierten Spiele: {num_games}")
print(f"Durchschnittliche Züge pro Spiel: {total_turns / num_games:.2f}")
print(f"Durchschnittlich gespielte Karten pro Spiel: {total_cards_played / num_games:.2f}")
print("\nGewinnstatistiken:")
for player, wins in win_counts.items():
    print(f"Spieler {player}: {wins} Siege ({wins/num_games*100:.2f}%)")

print("\nDie grafische Darstellung wurde als 'uno_results.png' gespeichert.")

# Zusätzliche Statistiken
longest_streak = max(len(list(g)) for k, g in itertools.groupby(results))
print(f"\nLängste Siegesserie eines Spielers: {longest_streak}")

most_common_winner = Counter(results).most_common(1)[0]
print(f"Häufigster Gewinner: Spieler {most_common_winner[0]} (Siege: {most_common_winner[1]})")

print("\nHinweis: Diese Simulation basiert auf vereinfachten Uno-Regeln und zufälligem Spielverhalten.")
print("Für genauere Ergebnisse könnte die Spiellogik erweitert und die Anzahl der Simulationen erhöht werden.")